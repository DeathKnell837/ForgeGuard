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
IMG_SIZE = (128, 128)
TEST_SIZE_AUTH = 75
TEST_SIZE_FORGED_EDITED = 37
TEST_SIZE_FORGED_GEN = 38
TEST_SIZE_TOTAL = 150  # exactly 50% authentic, 50% forged

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

def preprocess_image(fpath):
    """Load image, compute ELA, resize to 128x128, normalize to [0, 1]."""
    with Image.open(fpath) as img:
        ela = compute_ela(img)
        ela_resized = ela.resize(IMG_SIZE, Image.Resampling.BILINEAR)
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
    """Sample exactly 75 authentic, 37 edited, and 38 generated receipts using fixed seed."""
    rng = random.Random(seed)
    sampled_auth = rng.sample(auth_files, TEST_SIZE_AUTH)
    sampled_edited = rng.sample(edited_files, TEST_SIZE_FORGED_EDITED)
    sampled_gen = rng.sample(gen_files, TEST_SIZE_FORGED_GEN)
    
    # 0 = Authentic, 1 = Forged
    test_samples = [(f, 0) for f in sampled_auth] + [(f, 1) for f in sampled_edited] + [(f, 1) for f in sampled_gen]
    rng.shuffle(test_samples)
    return test_samples

def evaluate():
    print("=" * 75)
    print("ForgeGuard — 5-Seed Balanced Empirical Evaluation (Table 1 Alignment)")
    print("=" * 75)
    print(f"Test Partition Size: N = {TEST_SIZE_TOTAL} (75 Authentic, 75 Forged)")
    print(f"Predetermined Seeds: {SEEDS}")
    print("-" * 75)

    # 1. Load Models with @tf.function graph compilation
    model_definitions = [
        ('Basic_CNN', 'basic_cnn.keras', '~2.1M'),
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
        
        # 10 Warmup runs to compile graph & allocate CPU kernels
        dummy = np.zeros((1, 128, 128, 3), dtype=np.float32)
        for _ in range(10):
            _ = predict_fn(dummy)
        loaded_callables[name] = predict_fn
        print(f"  {name} compiled with @tf.function and warmed up.")

    process = psutil.Process(os.getpid())
    results_summary = {}

    for condition in ['Standard', 'Compressed']:
        print(f"\n=======================================================")
        print(f"EVALUATING CONDITION: {condition.upper()}")
        print(f"=======================================================")
        
        auth_files, edited_files, gen_files = collect_file_pools(condition)
        print(f"Available pools: {len(auth_files)} Authentic, {len(edited_files)} Edited, {len(gen_files)} Generated")

        for model_name, fname, params in model_definitions:
            predict_fn = loaded_callables[model_name]
            seed_runs = []

            print(f"\n--- Model: {model_name} | Condition: {condition} ---")

            for seed in SEEDS:
                test_samples = sample_balanced_test_set(auth_files, edited_files, gen_files, seed)
                y_true = []
                y_pred = []
                latencies = []
                memories_mb = []

                # Baseline memory before test batch
                baseline_rss = process.memory_info().rss / (1024 * 1024)

                for fpath, label in test_samples:
                    tensor = preprocess_image(fpath)
                    
                    # Timed inference with warm graph
                    t0 = time.perf_counter()
                    out = predict_fn(tensor)
                    dt_ms = (time.perf_counter() - t0) * 1000.0
                    
                    prob = float(out.numpy().flatten()[0])
                    pred_label = 1 if prob >= 0.5 else 0
                    
                    y_true.append(label)
                    y_pred.append(pred_label)
                    latencies.append(dt_ms)
                    
                    current_rss = process.memory_info().rss / (1024 * 1024)
                    memories_mb.append(current_rss)

                y_true = np.array(y_true)
                y_pred = np.array(y_pred)

                tp = int(np.sum((y_true == 1) & (y_pred == 1)))
                tn = int(np.sum((y_true == 0) & (y_pred == 0)))
                fp = int(np.sum((y_true == 0) & (y_pred == 1)))
                fn = int(np.sum((y_true == 1) & (y_pred == 0)))

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
                    'latency_ms': avg_lat,
                    'peak_memory_mb': peak_mem,
                    'tp': tp,
                    'tn': tn,
                    'fp': fp,
                    'fn': fn
                })

                print(f"  [Seed {seed}] Acc: {acc*100:.2f}% | Prec: {prec*100:.2f}% | Rec: {rec*100:.2f}% | F1: {f1*100:.2f}% | Lat: {avg_lat:.2f}ms | TP:{tp} TN:{tn} FP:{fp} FN:{fn}")

            # Calculate mean and standard deviation across 5 seeds
            accs = [r['accuracy'] for r in seed_runs]
            precs = [r['precision'] for r in seed_runs]
            recs = [r['recall'] for r in seed_runs]
            f1s = [r['f1_score'] for r in seed_runs]
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
