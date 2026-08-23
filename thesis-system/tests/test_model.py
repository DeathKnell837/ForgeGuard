"""Test CNN model inference directly"""
import sys, os
sys.path.insert(0, r"c:\Users\USER\Desktop\THESIS\thesis-system")

import numpy as np
from PIL import Image
from preprocessing.ela import compute_ela, convert_ela_to_array

MODELS_DIR = r"c:\Users\USER\Desktop\THESIS\thesis-system\models"
AUTHENTIC = r"c:\Users\USER\Desktop\THESIS\thesis-system\dataset\authentic\compressed\authentic_0001.jpg"
FORGED = r"c:\Users\USER\Desktop\THESIS\thesis-system\dataset\forged\compressed\amount_alteration\forged_amount_0001.jpg"

# Check model files exist
for name in ["basic_cnn.keras", "mobilenetv2.keras", "resnet50.keras"]:
    path = os.path.join(MODELS_DIR, name)
    exists = os.path.exists(path)
    size_mb = os.path.getsize(path) / (1024*1024) if exists else 0
    print(f"  {name}: {'EXISTS' if exists else 'MISSING'} ({size_mb:.1f} MB)")

print()

# Try loading model
try:
    import tensorflow as tf
    print(f"TensorFlow version: {tf.__version__}")
    
    model = tf.keras.models.load_model(os.path.join(MODELS_DIR, "mobilenetv2.keras"))
    print(f"Model loaded successfully! Input shape: {model.input_shape}")
    
    # Test authentic
    img = Image.open(AUTHENTIC).convert("RGB")
    ela = compute_ela(img, quality=90, scale=15.0)
    arr = convert_ela_to_array(ela, target_size=(128, 128))
    pred = float(model.predict(np.expand_dims(arr, 0), verbose=0)[0][0])
    verdict = "FORGED" if pred >= 0.5 else "AUTHENTIC"
    print(f"  Authentic receipt -> pred={pred:.4f} -> {verdict}")
    
    # Test forged
    img2 = Image.open(FORGED).convert("RGB")
    ela2 = compute_ela(img2, quality=90, scale=15.0)
    arr2 = convert_ela_to_array(ela2, target_size=(128, 128))
    pred2 = float(model.predict(np.expand_dims(arr2, 0), verbose=0)[0][0])
    verdict2 = "FORGED" if pred2 >= 0.5 else "AUTHENTIC"
    print(f"  Forged receipt   -> pred={pred2:.4f} -> {verdict2}")
    
except Exception as e:
    print(f"ERROR: {e}")
