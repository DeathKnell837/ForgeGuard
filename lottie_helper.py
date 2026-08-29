# -*- coding: utf-8 -*-
"""
ForgeGuard Lottie Animation Management Module
Provides local file and URL loaders, caching, and safe fallback rendering.
"""
import os
import json
import requests
import streamlit as st

try:
    from streamlit_lottie import st_lottie
    LOTTIE_AVAILABLE = True
except ImportError:
    LOTTIE_AVAILABLE = False


@st.cache_data(ttl=3600, show_spinner=False)
def load_lottie_url(url: str):
    """
    Fetch and cache a Lottie animation JSON from a direct URL.
    Returns python dictionary or None if unreachable.
    """
    if not url:
        return None
    try:
        r = requests.get(url, timeout=4)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return None


@st.cache_data(show_spinner=False)
def load_lottie_file(filepath: str):
    """
    Load a local Lottie JSON animation from disk.
    Searches current working dir, webapp dir, and assets dir.
    """
    if not filepath:
        return None
    
    candidates = [
        filepath,
        os.path.join(os.path.dirname(__file__), filepath),
        os.path.join(os.path.dirname(__file__), 'assets', filepath),
        os.path.join(os.path.dirname(__file__), 'assets', 'lottie', filepath),
    ]
    
    for p in candidates:
        if os.path.exists(p) and os.path.isfile(p):
            try:
                with open(p, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                pass
    return None


def render_lottie(lottie_data, height=120, width=None, key=None, loop=True, quality='high', speed=1.0):
    """
    Renders a Lottie animation using streamlit-lottie if available.
    Returns True if successfully rendered, False otherwise.
    """
    if not LOTTIE_AVAILABLE or not lottie_data:
        return False
    
    try:
        st_lottie(
            lottie_data,
            speed=speed,
            reverse=False,
            loop=loop,
            quality=quality,
            height=height,
            width=width,
            key=key
        )
        return True
    except Exception:
        return False
