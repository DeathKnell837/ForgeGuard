"""
ForgeGuard — Five-Seed Balanced Empirical Benchmark Evaluation
===============================================================
Canonically aligned with THESIS1UNGAB_BACANTO.md (Table 1, Section 2.3, 2.7, 2.8, 2.10):
- Fixed 25% Stratified Test Partition: Exactly 150 samples (75 Authentic, 75 Forged)
  - 75 Authentic GCash downloadable receipts
  - 75 Forged receipts: 37 Digitally Edited, 38 Programmatically Generated
- Replicated across 5 predetermined random seeds (30 evaluation runs total)
- Metrics reported as mean +/- standard deviation (mu +/- sigma)
- Dependent variables: Accuracy, Precision, Recall, F1-Score, Latency (ms), Peak Memory (MB)
- Discloses complete confusion matrices (including ResNet50 compression collapse)
"""

import os
import sys
import glob
import time
import json
import random
import io
import psutil
import numpy as np
from PIL import Image, ImageChops, ImageEnhance

# Set path and suppress TF logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
tf.get_logger().setLevel('ERROR')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(SCRIPT_DIR, 'models')
DATASET_DIR = os.path.join(SCRIPT_DIR, 'dataset')
OUTPUT_JSON_1 = os.path.join(MODELS_DIR, 'evaluation_metrics.json')
OUTPUT_JSON_2 = os.path.join(os.path.dirname(SCRIPT_DIR), 'models', 'evaluation_metrics.json')

SEEDS = [42, 101, 202, 303, 404]
IMG_SIZE = (224, 224)
TEST_SIZE_AUTH = 112
TEST_SIZE_FORGED_EDITED = 56
TEST_SIZE_FORGED_GEN = 57
TEST_SIZE_TOTAL = 225  # 112 Authentic, 56 Digitally Edited, 57 Programmatically/AI-Generated (Table 1 1:1 Balance)

DIGITAL_EDIT_CATEGORIES = ['amount_alteration', 'font_tampering', 'name_modification', 'ref_fabrication']
PROGRAMMATIC_GEN_CATEGORIES = ['ai_diffusion_generated', 'ai_generated_template', 'full_template']

def compute_ela(image, quality=90, scale=15.0):
    """Canonical Error Level Analysis (JPEG Q=90, scale multiplier 15.0x)."""
    if image.mode != 'RGB':
        image = image.convert('RGB')
    buf = io.BytesIO()
    image.save(buf, format='JPEG', quality=quality)
    buf.seek(0)
    resaved = Image.open(buf).convert('RGB')
    ela_diff = ImageChops.difference(image, resaved)
    return ImageEnhance.Brightness(ela_diff).enhance(scale)

def preprocess_image(fpath, target_size=IMG_SIZE):
    """Load image from disk, compute ELA, resize to target_size (default 224x224), normalize to [0, 1]."""
    with Image.open(fpath) as img:
        ela = compute_ela(img)
        ela_resized = ela.resize(target_size, Image.Resampling.BILINEAR)
        arr = np.array(ela_resized, dtype=np.float32) / 255.0
        return np.expand_dims(arr, axis=0)

VALID_EXTS = ('.png', '.jpg', '.jpeg', '.webp', '.bmp')

def collect_file_pools(condition):
    """Collect available image files categorized into Authentic, Edited, Generated."""
    cond_dir = 'highres' if condition == 'Standard' else 'compressed'
    
    auth_dir = os.path.join(DATASET_DIR, 'authentic', cond_dir)
    auth_files = [f for f in glob.glob(os.path.join(auth_dir, '*.*')) if f.lower().endswith(VALID_EXTS)]
    auth_files = sorted(auth_files)
    
    forged_dir = os.path.join(DATASET_DIR, 'forged', cond_dir)
    edited_files = []
    for cat in DIGITAL_EDIT_CATEGORIES:
        cat_dir = os.path.join(forged_dir, cat)
        if os.path.isdir(cat_dir):
            for ext in VALID_EXTS:
                edited_files.extend(glob.glob(os.path.join(cat_dir, '**', f'*{ext}'), recursive=True))
                edited_files.extend(glob.glob(os.path.join(cat_dir, '**', f'*{ext.upper()}'), recursive=True))
    edited_files = sorted(list(set(edited_files)))
    
    gen_files = []
    for cat in PROGRAMMATIC_GEN_CATEGORIES:
        cat_dir = os.path.join(forged_dir, cat)
        if os.path.isdir(cat_dir):
            for ext in VALID_EXTS:
                gen_files.extend(glob.glob(os.path.join(cat_dir, '**', f'*{ext}'), recursive=True))
                gen_files.extend(glob.glob(os.path.join(cat_dir, '**', f'*{ext.upper()}'), recursive=True))
    gen_files = sorted(list(set(gen_files)))
    
    return auth_files, edited_files, gen_files

def sample_balanced_test_set(auth_files, edited_files, gen_files, seed):
    """Sample exactly 112 authentic, 56 edited, and 57 AI-generated receipts using fixed seed (225 total)."""
    rng = random.Random(seed)
    sampled_auth = rng.sample(auth_files, TEST_SIZE_AUTH)
    sampled_edited = rng.sample(edited_files, TEST_SIZE_FORGED_EDITED)
    sampled_gen = rng.sample(gen_files, TEST_SIZE_FORGED_GEN)
    
    # 0 = Authentic, 1 = Forged, with explicit subtype tracking
    test_samples = (
        [(f, 0, 'authentic') for f in sampled_auth] +
        [(f, 1, 'edited') for f in sampled_edited] +
        [(f, 1, 'generated') for f in sampled_gen]
    )
    rng.shuffle(test_samples)
    return test_samples

def evaluate():
    print("=" * 75)
    print("ForgeGuard — 5-Seed Balanced Empirical Evaluation (Table 1 Alignment)")
    print("=" * 75)
    print(f"Test Partition Size: N = {TEST_SIZE_TOTAL} (112 Authentic, 56 Digitally Edited, 57 AI-Generated)")
    print(f"Predetermined Seeds: {SEEDS}")
    print("-" * 75)

    # 1. Load Models with @tf.function graph compilation
    model_definitions = [
        ('Basic_CNN', 'basic_cnn.keras', '~11.2M'),
        ('MobileNetV2', 'mobilenetv2.keras', '~3.4M'),
        ('ResNet50', 'resnet50.keras', '~23.5M'),
    ]

    loaded_callables = {}
    for name, fname, params in model_definitions:
        fpath = os.path.join(MODELS_DIR, fname)
        if not os.path.isfile(fpath):
            print(f"[ERROR] Missing model file: {fpath}")
            sys.exit(1)
        print(f"Loading {name} ({fname})...")
        m = tf.keras.models.load_model(fpath, compile=False)
        
        @tf.function
        def predict_fn(x, model=m):
            return model(x, training=False)
        
        in_shape = getattr(m, 'input_shape', None)
        model_img_size = (in_shape[1], in_shape[2]) if (in_shape and len(in_shape) == 4 and in_shape[1]) else IMG_SIZE
        
        # 10 Warmup runs to compile graph & allocate CPU kernels
        dummy = np.zeros((1, model_img_size[0], model_img_size[1], 3), dtype=np.float32)
        for _ in range(10):
            _ = predict_fn(dummy)
        loaded_callables[name] = (predict_fn, model_img_size)
        print(f"  {name} compiled with @tf.function (input size: {model_img_size}) and warmed up.")

    process = psutil.Process(os.getpid())
    results_summary = {}

    for condition in ['Standard', 'Compressed']:
        print(f"\n=======================================================")
        print(f"EVALUATING CONDITION: {condition.upper()}")
        print(f"=======================================================")
        
        auth_files, edited_files, gen_files = collect_file_pools(condition)
        print(f"Available pools: {len(auth_files)} Authentic, {len(edited_files)} Edited, {len(gen_files)} Generated")

        for model_name, fname, params in model_definitions:
            predict_fn, model_img_size = loaded_callables[model_name]
            seed_runs = []

            print(f"\n--- Model: {model_name} | Condition: {condition} ---")

            for seed in SEEDS:
                test_samples = sample_balanced_test_set(auth_files, edited_files, gen_files, seed)
                y_true = []
                y_pred = []
                subtypes = []
                latencies = []
                memories_mb = []

                # Baseline memory before test batch
                baseline_rss = process.memory_info().rss / (1024 * 1024)

                for fpath, label, subtype in test_samples:
                    # End-to-end processing time timing harness (file read through ELA preprocessing to prediction)
                    t0 = time.perf_counter()
                    tensor = preprocess_image(fpath, target_size=model_img_size)
                    out = predict_fn(tensor)
                    dt_ms = (time.perf_counter() - t0) * 1000.0
                    
                    prob = float(out.numpy().flatten()[0])
                    pred_label = 1 if prob >= 0.5 else 0
                    
                    y_true.append(label)
                    y_pred.append(pred_label)
                    subtypes.append(subtype)
                    latencies.append(dt_ms)
                    
                    current_rss = process.memory_info().rss / (1024 * 1024)
                    memories_mb.append(current_rss)

                y_true = np.array(y_true)
                y_pred = np.array(y_pred)
                subtypes = np.array(subtypes)

                tp = int(np.sum((y_true == 1) & (y_pred == 1)))
                tn = int(np.sum((y_true == 0) & (y_pred == 0)))
                fp = int(np.sum((y_true == 0) & (y_pred == 1)))
                fn = int(np.sum((y_true == 1) & (y_pred == 0)))

                # Subtype-specific metrics (Section 2.8 P258)
                edited_mask = (subtypes == 'edited')
                gen_mask = (subtypes == 'generated')
                auth_mask = (subtypes == 'authentic')

                edited_tp = int(np.sum((y_true[edited_mask] == 1) & (y_pred[edited_mask] == 1)))
                edited_fn = int(np.sum((y_true[edited_mask] == 1) & (y_pred[edited_mask] == 0)))
                edited_rec = float(edited_tp / np.sum(edited_mask)) if np.sum(edited_mask) > 0 else 0.0

                gen_tp = int(np.sum((y_true[gen_mask] == 1) & (y_pred[gen_mask] == 1)))
                gen_fn = int(np.sum((y_true[gen_mask] == 1) & (y_pred[gen_mask] == 0)))
                gen_rec = float(gen_tp / np.sum(gen_mask)) if np.sum(gen_mask) > 0 else 0.0

                auth_tn = int(np.sum((y_true[auth_mask] == 0) & (y_pred[auth_mask] == 0)))
                auth_spec = float(auth_tn / np.sum(auth_mask)) if np.sum(auth_mask) > 0 else 0.0

                acc = (tp + tn) / TEST_SIZE_TOTAL
                prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
                rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
                f1 = (2 * prec * rec) / (prec + rec) if (prec + rec) > 0 else 0.0
                avg_lat = float(np.mean(latencies))
                peak_mem = float(np.max(memories_mb))

                seed_runs.append({
                    'seed': seed,
                    'accuracy': acc,
                    'precision': prec,
                    'recall': rec,
                    'f1_score': f1,
                    'edited_recall': edited_rec,
                    'generated_recall': gen_rec,
                    'authentic_specificity': auth_spec,
                    'latency_ms': avg_lat,
                    'peak_memory_mb': peak_mem,
                    'tp': tp,
                    'tn': tn,
                    'fp': fp,
                    'fn': fn,
                    'edited_tp': edited_tp,
                    'edited_fn': edited_fn,
                    'gen_tp': gen_tp,
                    'gen_fn': gen_fn
                })

                print(f"  [Seed {seed}] Acc: {acc*100:.2f}% | Prec: {prec*100:.2f}% | Rec: {rec*100:.2f}% | F1: {f1*100:.2f}% | EdRec: {edited_rec*100:.1f}% | GenRec: {gen_rec*100:.1f}% | Lat: {avg_lat:.2f}ms")

            # Calculate mean and standard deviation across 5 seeds
            accs = [r['accuracy'] for r in seed_runs]
            precs = [r['precision'] for r in seed_runs]
            recs = [r['recall'] for r in seed_runs]
            f1s = [r['f1_score'] for r in seed_runs]
            ed_recs = [r['edited_recall'] for r in seed_runs]
            gen_recs = [r['generated_recall'] for r in seed_runs]
            auth_specs = [r['authentic_specificity'] for r in seed_runs]
            lats = [r['latency_ms'] for r in seed_runs]
            mems = [r['peak_memory_mb'] for r in seed_runs]
            tps = [r['tp'] for r in seed_runs]
            tns = [r['tn'] for r in seed_runs]
            fps = [r['fp'] for r in seed_runs]
            fns = [r['fn'] for r in seed_runs]

            key = model_name if condition == 'Standard' else f"{model_name}_Compressed"
            results_summary[key] = {
                'architecture': model_name.replace('_', ' '),
                'condition': condition,
                'accuracy': round(float(np.mean(accs)), 4),
                'accuracy_std': round(float(np.std(accs)), 4),
                'precision': round(float(np.mean(precs)), 4),
                'precision_std': round(float(np.std(precs)), 4),
                'recall': round(float(np.mean(recs)), 4),
                'recall_std': round(float(np.std(recs)), 4),
                'f1_score': round(float(np.mean(f1s)), 4),
                'f1_std': round(float(np.std(f1s)), 4),
                'edited_recall': round(float(np.mean(ed_recs)), 4),
                'edited_recall_std': round(float(np.std(ed_recs)), 4),
                'generated_recall': round(float(np.mean(gen_recs)), 4),
                'generated_recall_std': round(float(np.std(gen_recs)), 4),
                'authentic_specificity': round(float(np.mean(auth_specs)), 4),
                'authentic_specificity_std': round(float(np.std(auth_specs)), 4),
                'latency_ms': round(float(np.mean(lats)), 2),
                'latency_ms_std': round(float(np.std(lats)), 2),
                'peak_memory_mb': round(float(np.mean(mems)), 2),
                'peak_memory_mb_std': round(float(np.std(mems)), 2),
                'params': params,
                'test_size': TEST_SIZE_TOTAL,
                'authentic_test_count': TEST_SIZE_AUTH,
                'forged_test_count': TEST_SIZE_FORGED_EDITED + TEST_SIZE_FORGED_GEN,
                'confusion': {
                    'tp': int(round(float(np.mean(tps)))),
                    'tn': int(round(float(np.mean(tns)))),
                    'fp': int(round(float(np.mean(fps)))),
                    'fn': int(round(float(np.mean(fns))))
                },
                'seed_runs': seed_runs
            }

            print(f">> MEAN ({condition}): Acc: {np.mean(accs)*100:.2f}% +/- {np.std(accs)*100:.2f}% | Lat: {np.mean(lats):.2f} +/- {np.std(lats):.2f} ms | Mem: {np.mean(mems):.1f} MB")

    # 3. Compute Section 2.10 Weighted Min-Max Composite Score for Research Question 5
    # Formula: 0.50 * Norm_Accuracy + 0.25 * Norm_Latency_Efficiency + 0.25 * Norm_Memory_Efficiency
    print("\n-------------------------------------------------------")
    print("COMPUTING SECTION 2.10 COMPOSITE SCORES (RQ5)")
    print("-------------------------------------------------------")
    for condition in ['Standard', 'Compressed']:
        cond_keys = [
            (m if condition == 'Standard' else f"{m}_Compressed")
            for m, _, _ in model_definitions
        ]
        acc_vals = [results_summary[k]['accuracy'] for k in cond_keys]
        lat_vals = [results_summary[k]['latency_ms'] for k in cond_keys]
        mem_vals = [results_summary[k]['peak_memory_mb'] for k in cond_keys]

        min_acc, max_acc = min(acc_vals), max(acc_vals)
        min_lat, max_lat = min(lat_vals), max(lat_vals)
        min_mem, max_mem = min(mem_vals), max(mem_vals)

        for k in cond_keys:
            acc = results_summary[k]['accuracy']
            lat = results_summary[k]['latency_ms']
            mem = results_summary[k]['peak_memory_mb']

            norm_acc = (acc - min_acc) / (max_acc - min_acc) if max_acc > min_acc else 1.0
            norm_lat = (max_lat - lat) / (max_lat - min_lat) if max_lat > min_lat else 1.0
            norm_mem = (max_mem - mem) / (max_mem - min_mem) if max_mem > min_mem else 1.0

            comp_score = 0.50 * norm_acc + 0.25 * norm_lat + 0.25 * norm_mem
            comp_score_pct = round(comp_score * 100.0, 2)

            results_summary[k]['composite_score'] = round(comp_score, 4)
            results_summary[k]['composite_score_pct'] = comp_score_pct
            results_summary[k]['norm_accuracy'] = round(norm_acc, 4)
            results_summary[k]['norm_latency'] = round(norm_lat, 4)
            results_summary[k]['norm_memory'] = round(norm_mem, 4)

            print(f"[{condition}] {k}: Composite Score = {comp_score_pct:.2f}% (Acc: {acc*100:.2f}%, Lat: {lat:.1f}ms, Mem: {mem:.1f}MB)")

    # 4. Save to JSON files
    for out_path in [OUTPUT_JSON_1, OUTPUT_JSON_2]:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(results_summary, f, indent=2)
        print(f"\n[SAVED] Benchmark metrics written to: {out_path}")

    print("\n=======================================================")
    print("5-SEED BALANCED EMPIRICAL BENCHMARK COMPLETE")
    print("=======================================================")

if __name__ == '__main__':
    evaluate()
