"""
Evaluate all three CNN architectures on the Compressed condition dataset.
Outputs metrics to evaluation_metrics.json (adds compressed keys).
"""
import os
import sys
import json
import time
import io
import numpy as np
from PIL import Image, ImageChops, ImageEnhance

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(SCRIPT_DIR, 'models')
DATASET_DIR = os.path.join(SCRIPT_DIR, 'dataset')
METRICS_PATH = os.path.join(MODELS_DIR, 'evaluation_metrics.json')

# ELA function (same as app.py)
def compute_ela(image, quality=90, scale=15.0):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    buf = io.BytesIO()
    image.save(buf, format='JPEG', quality=quality)
    buf.seek(0)
    resaved = Image.open(buf).convert('RGB')
    ela_diff = ImageChops.difference(image, resaved)
    return ImageEnhance.Brightness(ela_diff).enhance(scale)

def load_images_from_dir(directory, label):
    """Load all images from directory (and subdirectories), return (image, label) pairs."""
    pairs = []
    if not os.path.isdir(directory):
        print(f"  [SKIP] Directory not found: {directory}")
        return pairs
    for root, dirs, files in os.walk(directory):
        for fname in files:
            if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp')):
                fpath = os.path.join(root, fname)
                try:
                    img = Image.open(fpath).convert('RGB')
                    pairs.append((img, label))
                except Exception as e:
                    print(f"  [WARN] Failed to load {fpath}: {e}")
    return pairs

def preprocess_for_model(image):
    """ELA -> resize 128x128 -> normalize -> batch dimension."""
    ela = compute_ela(image)
    ela_resized = ela.resize((128, 128), Image.Resampling.BILINEAR)
    arr = np.array(ela_resized, dtype=np.float32) / 255.0
    return np.expand_dims(arr, axis=0)

def main():
    print("=" * 60)
    print("ForgeGuard - Compressed Dataset Evaluation")
    print("=" * 60)
    
    # Load compressed datasets
    auth_dir = os.path.join(DATASET_DIR, 'authentic', 'compressed')
    forged_dir = os.path.join(DATASET_DIR, 'forged', 'compressed')
    
    print(f"\nLoading authentic compressed from: {auth_dir}")
    auth_pairs = load_images_from_dir(auth_dir, 0)  # 0 = authentic
    print(f"  Loaded {len(auth_pairs)} authentic images")
    
    print(f"\nLoading forged compressed from: {forged_dir}")
    forged_pairs = load_images_from_dir(forged_dir, 1)  # 1 = forged
    print(f"  Loaded {len(forged_pairs)} forged images")
    
    all_pairs = auth_pairs + forged_pairs
    total = len(all_pairs)
    print(f"\nTotal compressed dataset: {total} images ({len(auth_pairs)} authentic + {len(forged_pairs)} forged)")
    
    if total == 0:
        print("[ERROR] No images found. Aborting.")
        sys.exit(1)
    
    # Import TF and load models
    print("\nLoading TensorFlow and models...")
    import tensorflow as tf
    tf.get_logger().setLevel('ERROR')
    
    model_files = {
        'Basic_CNN': 'basic_cnn.keras',
        'MobileNetV2': 'mobilenetv2.keras',
        'ResNet50': 'resnet50.keras'
    }
    
    models = {}
    for name, fname in model_files.items():
        fpath = os.path.join(MODELS_DIR, fname)
        if os.path.isfile(fpath):
            print(f"  Loading {name} from {fname}...")
            m = tf.keras.models.load_model(fpath, compile=False)
            models[name] = m
        else:
            print(f"  [WARN] Model file not found: {fpath}")
    
    if not models:
        print("[ERROR] No models loaded. Aborting.")
        sys.exit(1)
    
    # Warm up models
    print("\nWarming up models...")
    dummy = np.zeros((1, 128, 128, 3), dtype=np.float32)
    for name, m in models.items():
        _ = m(dummy, training=False)
        print(f"  Warmed up {name}")
    
    # Evaluate each model
    results = {}
    
    for model_name, model in models.items():
        print(f"\n{'='*40}")
        print(f"Evaluating {model_name} on compressed dataset...")
        print(f"{'='*40}")
        
        y_true = []
        y_pred = []
        latencies = []
        
        for idx, (img, label) in enumerate(all_pairs):
            input_tensor = preprocess_for_model(img)
            
            t0 = time.perf_counter()
            pred = model(input_tensor, training=False)
            dt = (time.perf_counter() - t0) * 1000.0
            
            pred_val = float(pred.numpy().flatten()[0])
            predicted_label = 1 if pred_val >= 0.5 else 0
            
            y_true.append(label)
            y_pred.append(predicted_label)
            latencies.append(dt)
            
            if (idx + 1) % 100 == 0 or (idx + 1) == total:
                print(f"  Progress: {idx+1}/{total}")
        
        # Compute metrics
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)
        
        tp = int(np.sum((y_true == 1) & (y_pred == 1)))
        tn = int(np.sum((y_true == 0) & (y_pred == 0)))
        fp = int(np.sum((y_true == 0) & (y_pred == 1)))
        fn = int(np.sum((y_true == 1) & (y_pred == 0)))
        
        accuracy = (tp + tn) / total if total > 0 else 0
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        avg_latency = float(np.mean(latencies))
        
        print(f"\n  Results for {model_name}:")
        print(f"    Accuracy:  {accuracy*100:.2f}%")
        print(f"    Precision: {precision*100:.2f}%")
        print(f"    Recall:    {recall*100:.2f}%")
        print(f"    F1 Score:  {f1*100:.2f}%")
        print(f"    Avg Latency: {avg_latency:.2f} ms")
        print(f"    Confusion: TP={tp}, TN={tn}, FP={fp}, FN={fn}")
        
        compressed_key = f"{model_name}_Compressed"
        results[compressed_key] = {
            "accuracy": round(accuracy, 4),
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1_score": round(f1, 4),
            "latency_ms": round(avg_latency, 2),
            "confusion": {"tp": tp, "tn": tn, "fp": fp, "fn": fn},
            "dataset_size": total,
            "authentic_count": len(auth_pairs),
            "forged_count": len(forged_pairs)
        }
    
    # Merge with existing metrics
    print(f"\nLoading existing metrics from {METRICS_PATH}...")
    if os.path.isfile(METRICS_PATH):
        with open(METRICS_PATH, 'r') as f:
            existing = json.load(f)
    else:
        existing = {}
    
    existing.update(results)
    
    with open(METRICS_PATH, 'w') as f:
        json.dump(existing, f, indent=2)
    
    print(f"\nMetrics saved to {METRICS_PATH}")
    print("\nFinal metrics file contents:")
    print(json.dumps(existing, indent=2))
    print("\nEvaluation complete.")

if __name__ == '__main__':
    main()
