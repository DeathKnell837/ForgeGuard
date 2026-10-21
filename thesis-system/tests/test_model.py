"""Test CNN model inference directly across all architectures"""
import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
sys.path.insert(0, BASE_DIR)

import numpy as np
from PIL import Image
from preprocessing.ela import compute_ela, convert_ela_to_array

MODELS_DIR = os.path.join(BASE_DIR, "models")
AUTHENTIC = os.path.join(BASE_DIR, "dataset", "authentic", "compressed", "authentic_0001.jpg")
FORGED = os.path.join(BASE_DIR, "dataset", "forged", "compressed", "amount_alteration", "forged_amount_0001.jpg")

# Check model files exist
print("Checking model files in:", MODELS_DIR)
for name in ["basic_cnn.keras", "mobilenetv2.keras", "resnet50.keras"]:
    path = os.path.join(MODELS_DIR, name)
    exists = os.path.exists(path)
    size_mb = os.path.getsize(path) / (1024*1024) if exists else 0
    print(f"  {name}: {'EXISTS' if exists else 'MISSING'} ({size_mb:.1f} MB)")

print()

try:
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    import tensorflow as tf
    tf.get_logger().setLevel('ERROR')
    print(f"TensorFlow version: {tf.__version__}")
    
    for model_name, fname in [
        ("Basic CNN", "basic_cnn.keras"),
        ("MobileNetV2", "mobilenetv2.keras"),
        ("ResNet50", "resnet50.keras")
    ]:
        mpath = os.path.join(MODELS_DIR, fname)
        if not os.path.isfile(mpath):
            print(f"Skipping {model_name} (file not found)")
            continue
            
        model = tf.keras.models.load_model(mpath, compile=False)
        in_shape = getattr(model, 'input_shape', None)
        target_size = (in_shape[1], in_shape[2]) if (in_shape and len(in_shape) == 4 and in_shape[1]) else (224, 224)
        print(f"\n--- {model_name} (shape: {target_size}) ---")
        
        # Test authentic
        img = Image.open(AUTHENTIC).convert("RGB")
        ela = compute_ela(img, quality=90, scale=15.0)
        arr = convert_ela_to_array(ela, target_size=target_size)
        pred = float(model.predict(np.expand_dims(arr, 0), verbose=0)[0][0])
        verdict = "FORGED" if pred >= 0.5 else "AUTHENTIC"
        print(f"  Authentic receipt -> pred={pred:.4f} -> {verdict}")
        
        # Test forged
        img2 = Image.open(FORGED).convert("RGB")
        ela2 = compute_ela(img2, quality=90, scale=15.0)
        arr2 = convert_ela_to_array(ela2, target_size=target_size)
        pred2 = float(model.predict(np.expand_dims(arr2, 0), verbose=0)[0][0])
        verdict2 = "FORGED" if pred2 >= 0.5 else "AUTHENTIC"
        print(f"  Forged receipt   -> pred={pred2:.4f} -> {verdict2}")

except Exception as e:
    print(f"ERROR: {e}")
