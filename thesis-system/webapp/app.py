"""
ForgeGuard — CNN Receipt Classification Demo
=============================================
BSCS Thesis: "Securing Mobile Transaction: A Comparative Evaluation of
CNN Architectures in Detecting Digital Receipt Forgery"
Notre Dame of Midsayap College (NDMC) | CITE
Authors: Ungab & Bacanto | Adviser: Ms. Doris Ann Mariano
"""

import os
import sys
import json
import io
import time
import numpy as np
from PIL import Image, ImageChops, ImageEnhance
import streamlit as st

# --- Path Setup ---
APP_DIR = os.path.dirname(os.path.abspath(__file__))
# Walk up to find thesis-system or models directory
if os.path.exists(os.path.join(APP_DIR, 'models')):
    SYS_DIR = APP_DIR
elif os.path.exists(os.path.join(APP_DIR, '..', 'models')):
    SYS_DIR = os.path.abspath(os.path.join(APP_DIR, '..'))
else:
    SYS_DIR = os.path.abspath(os.path.join(APP_DIR, '..'))

for p in [APP_DIR, SYS_DIR]:
    if p not in sys.path:
        sys.path.insert(0, p)

# --- CSS ---
try:
    from premium_css import PREMIUM_CSS
except ImportError:
    PREMIUM_CSS = ''

# --- Page Config ---
st.set_page_config(
    page_title='ForgeGuard | CNN Receipt Classification Demo',
    page_icon=None,
    layout='wide',
    initial_sidebar_state='collapsed'
)
st.markdown(PREMIUM_CSS, unsafe_allow_html=True)

def render_html(html_str):
    """Strip leading and trailing whitespace from every line so Markdown parser renders raw HTML instead of code blocks."""
    cleaned = "".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)

# --- Model Loading ---
@st.cache_resource
def load_tf_model(path):
    """Load a .keras model file using TensorFlow or Keras."""
    if not os.path.isfile(path):
        st.error(f'Model file not found: {os.path.basename(path)}')
        return None
    try:
        import tensorflow as tf
        tf.get_logger().setLevel('ERROR')
        return tf.keras.models.load_model(path, compile=False)
    except ModuleNotFoundError:
        try:
            import keras
            return keras.models.load_model(path, compile=False)
        except Exception:
            st.error(f'TensorFlow runtime is installing/initializing on Streamlit Cloud. Please wait a moment and refresh.')
            return None
    except Exception as e:
        try:
            import keras
            return keras.models.load_model(path, compile=False)
        except Exception:
            st.error(f'Failed to load model {os.path.basename(path)}: {e}')
            return None

def get_model_paths():
    """Find the model files across candidate directory locations."""
    candidates = [
        os.path.join(SYS_DIR, 'models'),
        os.path.join(APP_DIR, 'models'),
        os.path.join(os.path.dirname(SYS_DIR), 'models'),
        os.path.join(os.path.dirname(APP_DIR), 'models'),
        os.path.join(os.path.dirname(os.path.dirname(APP_DIR)), 'models'),
        os.path.join(os.path.dirname(os.path.dirname(APP_DIR)), 'thesis-system', 'models'),
    ]
    models_dir = None
    for cand in candidates:
        if os.path.isdir(cand) and os.path.isfile(os.path.join(cand, 'basic_cnn.keras')):
            models_dir = cand
            break
    if not models_dir:
        models_dir = os.path.join(SYS_DIR, 'models')

    return {
        'Basic CNN': os.path.join(models_dir, 'basic_cnn.keras'),
        'ResNet50': os.path.join(models_dir, 'resnet50.keras'),
        'MobileNetV2': os.path.join(models_dir, 'mobilenetv2.keras'),
    }

def get_model_info():
    """Architecture metadata."""
    return {
        'Basic CNN': {'params': '~2.1M', 'arch': 'Custom 3-layer sequential CNN'},
        'ResNet50': {'params': '~23.5M', 'arch': '50-layer deep residual network'},
        'MobileNetV2': {'params': '~3.4M', 'arch': 'Lightweight inverted residual blocks'},
    }

# --- ELA Functions ---
def compute_ela(image, quality=90, scale=15.0):
    """Compute Error Level Analysis."""
    if image.mode != 'RGB':
        image = image.convert('RGB')
    buf = io.BytesIO()
    image.save(buf, format='JPEG', quality=quality)
    buf.seek(0)
    resaved = Image.open(buf).convert('RGB')
    ela_diff = ImageChops.difference(image, resaved)
    return ImageEnhance.Brightness(ela_diff).enhance(scale)

def convert_ela_to_array(ela_image, target_size=(128, 128)):
    """Convert ELA image to normalized array for model input."""
    resized = ela_image.resize(target_size, Image.Resampling.BILINEAR)
    return np.array(resized, dtype=np.float32) / 255.0

# --- Inference Function ---
def run_inference(image, model, model_name):
    """
    Run a single model inference on an uploaded image.
    Returns dict with verdict, confidence, latency.
    """
    if model is None:
        return {'verdict': 'Error', 'confidence': 0.0, 'latency_ms': 0.0, 'error': True}
    
    # Compute ELA
    ela = compute_ela(image)
    ela_arr = convert_ela_to_array(ela, target_size=(128, 128))
    input_tensor = np.expand_dims(ela_arr, axis=0)  # (1, 128, 128, 3)
    
    # Inference with timing
    start = time.perf_counter()
    prediction = model.predict(input_tensor, verbose=0)
    elapsed_ms = (time.perf_counter() - start) * 1000.0
    
    # Sigmoid output: >= 0.5 means Forged, < 0.5 means Authentic
    prob = float(prediction[0][0]) if prediction.shape[-1] == 1 else float(prediction[0][1])
    
    if prob >= 0.5:
        verdict = 'Forged'
        confidence = prob * 100.0
    else:
        verdict = 'Authentic'
        confidence = (1.0 - prob) * 100.0
    
    return {
        'verdict': verdict,
        'confidence': confidence,
        'latency_ms': elapsed_ms,
        'raw_prob': prob,
        'error': False
    }

# --- Out-of-Domain Check ---
def check_out_of_domain(image):
    """
    Heuristic check if the uploaded image looks like a GCash receipt.
    Returns True if it deviates from expected receipt characteristics.
    Does NOT block inference or change any verdict.
    """
    w, h = image.size
    aspect = h / w if w > 0 else 1.0
    # GCash downloadable receipts are typically tall portrait (aspect ~1.5-3.0)
    if aspect < 1.2 or aspect > 4.0:
        return True
    # Very small images unlikely to be real receipts
    if w < 200 or h < 300:
        return True
    return False

# --- Metrics Loading ---
def load_evaluation_metrics():
    """Load evaluation_metrics.json."""
    for candidate in [
        os.path.join(SYS_DIR, 'models', 'evaluation_metrics.json'),
        os.path.join(os.path.dirname(SYS_DIR), 'models', 'evaluation_metrics.json'),
    ]:
        if os.path.isfile(candidate):
            with open(candidate, 'r') as f:
                return json.load(f)
    return {}

# --- Sidebar ---
with st.sidebar:
    st.markdown(
        '<div style="padding: 20px 16px 8px 16px;">'
        '<div style="font-size: 11px; text-transform: uppercase; letter-spacing: 2px; '
        'color: #94A3B8; margin-bottom: 16px;">Navigation</div>'
        '</div>',
        unsafe_allow_html=True
    )
    page = st.radio(
        'Select page',
        ['Classify a Receipt', 'Model Comparison'],
        label_visibility='collapsed'
    )
    
    st.markdown('<hr style="border: none; border-top: 1px solid rgba(255,255,255,0.06); margin: 24px 16px;">', unsafe_allow_html=True)
    
    # Footer info in sidebar
    st.markdown(
        '<div style="padding: 8px 16px; font-size: 11px; color: #64748B; line-height: 1.6;">'
        'NDMC BSCS Thesis 2026<br>'
        'Ungab &amp; Bacanto<br>'
        'Adviser: Ms. Mariano'
        '</div>',
        unsafe_allow_html=True
    )

# --- Screens ---
if page == 'Classify a Receipt':
    # Header section
    st.markdown(
        '<div>'
        '<div style="font-size: 32px; font-weight: 700; font-family: Inter, sans-serif;">ForgeGuard</div>'
        '<div style="font-size: 18px; color: #94A3B8; margin-bottom: 4px;">CNN Receipt Classification Demo</div>'
        '<div style="font-size: 12px; color: #64748B; margin-bottom: 4px;">Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery</div>'
        '<div style="font-size: 10px; color: #64748B; margin-bottom: 24px;">NDMC BSCS Thesis, 2026</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    uploaded = st.file_uploader(
        'Upload a GCash downloadable transaction receipt',
        type=['png', 'jpg', 'jpeg', 'webp']
    )
    
    if uploaded is not None:
        try:
            image = Image.open(uploaded).convert('RGB')
            col1, col2 = st.columns([0.35, 0.65])
            with col1:
                st.image(image, use_container_width=True)
                render_html(
                    '<div style="margin-top: 12px; font-family: \'JetBrains Mono\', monospace; font-size: 12px; color: #94A3B8;">'
                    '<div>Input resolution: 128 x 128 px (ELA-transformed)</div>'
                    '<div>Decision threshold: 0.5 (sigmoid)</div>'
                    '</div>'
                )
                
            with col2:
                model_paths = get_model_paths()
                model_info = get_model_info()
                
                with st.spinner('Analyzing receipt...'):
                    for model_name, path in model_paths.items():
                        model = load_tf_model(path)
                        result = run_inference(image, model, model_name)
                        
                        arch_description = model_info.get(model_name, {}).get('arch', '')
                        
                        if result['error']:
                            st.error(f'Error running inference on {model_name}.')
                            continue
                        
                        verdict = result['verdict']
                        confidence = result['confidence']
                        latency = result['latency_ms']
                        
                        verdict_lower = verdict.lower()
                        verdict_color = '#10B981' if verdict == 'Authentic' else '#EF4444'
                        
                        render_html(
                            f'''
                            <div class="fg-result-card fg-verdict-{verdict_lower}" style="background-color: #1C2333; padding: 16px; border-radius: 8px; margin-bottom: 16px; border-left: 4px solid {verdict_color};">
                              <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                  <div class="fg-model-name" style="font-weight: 700; font-size: 16px; color: #E2E8F0;">{model_name}</div>
                                  <div style="font-size: 12px; color: #94A3B8;">{arch_description}</div>
                                </div>
                                <div style="text-align: right;">
                                  <div class="fg-verdict-label" style="color: {verdict_color}; font-weight: 700; font-size: 18px;">{verdict}</div>
                                  <div class="fg-confidence" style="font-size: 28px; font-weight: 700; color: {verdict_color};">{confidence:.1f}%</div>
                                  <div class="fg-latency" style="font-family: \'JetBrains Mono\', monospace; font-size: 12px; color: #94A3B8;">{latency:.1f} ms</div>
                                </div>
                              </div>
                            </div>
                            '''
                        )
                        
            if check_out_of_domain(image):
                render_html(
                    '<div class="fg-advisory" style="margin-top: 24px; padding: 12px; background-color: rgba(239, 68, 68, 0.1); border-left: 4px solid #EF4444; color: #E2E8F0; font-size: 14px;">'
                    'Note: This image deviates from standard GCash downloadable receipt '
                    'characteristics. Evaluated under standard binary classification.'
                    '</div>'
                )
                
        except Exception as e:
            st.error(f'Error processing image: {str(e)}')

elif page == 'Model Comparison':
    st.markdown(
        '<div>'
        '<div style="font-size: 32px; font-weight: 700; font-family: Inter, sans-serif;">ForgeGuard</div>'
        '<div style="font-size: 18px; color: #94A3B8; margin-bottom: 24px;">Model Performance Comparison</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    metrics = load_evaluation_metrics()
    model_info = get_model_info()
    
    if not metrics:
        st.info('Evaluation metrics data not found.')
    else:
        st.markdown('<h3 style="font-size: 18px; margin-bottom: 16px;">Overall Performance</h3>', unsafe_allow_html=True)
        
        # Build HTML table for metrics
        table_html = '''
        <table class="fg-metrics-table" style="width: 100%; border-collapse: collapse; text-align: left; margin-bottom: 32px; background-color: #1C2333; color: #E2E8F0;">
            <thead>
                <tr style="border-bottom: 1px solid #334155; font-size: 14px;">
                    <th style="padding: 12px;">Architecture</th>
                    <th style="padding: 12px;">Condition</th>
                    <th style="padding: 12px;">Accuracy</th>
                    <th style="padding: 12px;">Precision</th>
                    <th style="padding: 12px;">Recall</th>
                    <th style="padding: 12px;">F1</th>
                    <th style="padding: 12px;">Latency (ms)</th>
                    <th style="padding: 12px;">Params</th>
                </tr>
            </thead>
            <tbody>
        '''
        
        for raw_model_name, data in metrics.items():
            model_name = raw_model_name.replace('_', ' ')
            params = model_info.get(model_name, {}).get('params', 'N/A')
            
            # Standard Condition
            table_html += f'''
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); font-family: 'JetBrains Mono', monospace; font-size: 13px;">
                <td style="padding: 12px; font-family: Inter, sans-serif; font-weight: 600;">{model_name}</td>
                <td style="padding: 12px; font-family: Inter, sans-serif;">Standard</td>
                <td style="padding: 12px;">{data.get('accuracy', 0)*100:.2f}%</td>
                <td style="padding: 12px;">{data.get('precision', 0)*100:.2f}%</td>
                <td style="padding: 12px;">{data.get('recall', 0)*100:.2f}%</td>
                <td style="padding: 12px;">{data.get('f1_score', 0)*100:.2f}%</td>
                <td style="padding: 12px;">{data.get('latency_ms', 0.0):.2f}</td>
                <td style="padding: 12px;">{params}</td>
            </tr>
            '''
            
            # Compressed Condition
            table_html += f'''
            <tr style="border-bottom: 1px solid #334155; font-family: 'JetBrains Mono', monospace; font-size: 13px;">
                <td style="padding: 12px;"></td>
                <td style="padding: 12px; font-family: Inter, sans-serif;">Compressed</td>
                <td colspan="6" style="padding: 12px; font-family: Inter, sans-serif; font-style: italic; color: #64748B;">Not yet evaluated</td>
            </tr>
            '''
            
        table_html += '</tbody></table>'
        render_html(table_html)
        
    st.markdown('<h3 style="font-size: 18px; margin-bottom: 16px;">Confusion Matrix</h3>', unsafe_allow_html=True)
    selected_model = st.selectbox('Select Architecture', ['Basic CNN', 'ResNet50', 'MobileNetV2'])
    render_html(
        '<div style="padding: 32px; text-align: center; background-color: #1C2333; border-radius: 8px; color: #94A3B8; margin-bottom: 32px;">'
        'Confusion matrix data will be available after five-seed evaluation is complete.'
        '</div>'
    )
    
    st.markdown('<h3 style="font-size: 18px; margin-bottom: 16px;">Dataset Composition (Table 1)</h3>', unsafe_allow_html=True)
    dataset_html = '''
    <table style="width: 100%; max-width: 600px; border-collapse: collapse; text-align: left; background-color: #1C2333; color: #E2E8F0;">
        <thead>
            <tr style="border-bottom: 1px solid #334155; font-size: 14px;">
                <th style="padding: 12px;">Category</th>
                <th style="padding: 12px; text-align: right;">Count</th>
            </tr>
        </thead>
        <tbody>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); font-size: 14px;">
                <td style="padding: 12px;">Authentic (Downloadable GCash)</td>
                <td style="padding: 12px; text-align: right; font-family: 'JetBrains Mono', monospace;">300</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); font-size: 14px;">
                <td style="padding: 12px;">Forged (Digitally Edited)</td>
                <td style="padding: 12px; text-align: right; font-family: 'JetBrains Mono', monospace;">150</td>
            </tr>
            <tr style="border-bottom: 1px solid #334155; font-size: 14px;">
                <td style="padding: 12px;">Forged (Programmatically Generated)</td>
                <td style="padding: 12px; text-align: right; font-family: 'JetBrains Mono', monospace;">150</td>
            </tr>
            <tr style="font-weight: 700; font-size: 14px;">
                <td style="padding: 12px;">Total Base Images</td>
                <td style="padding: 12px; text-align: right; font-family: 'JetBrains Mono', monospace;">600</td>
            </tr>
        </tbody>
    </table>
    <div style="font-size: 12px; color: #94A3B8; margin-top: 12px; font-style: italic;">
    Note: Each base image is also evaluated under a Messenger-compressed condition.
    </div>
    '''
    render_html(dataset_html)
