import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
from modules import ai_analysis, report_tools, open_data, ui_utils, translations

# Page Config
st.set_page_config(
    page_title="OctoGreen",
    layout="wide",
    page_icon="assets/logo.png",
    initial_sidebar_state="collapsed"
)

# Apply CSS - Wrapped in hidden div to prevent display
st.markdown(f"""
<div style="display: none;">
{ui_utils.CUSTOM_CSS}
</div>
""", unsafe_allow_html=True)

# Also inject directly for backup
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg-gradient: linear-gradient(135deg, #eff6ff 0%, #dbeafe 50%, #bfdbfe 100%);
    --text-primary: #1d1d1f; /* Override to Apple's dark text */
    --text-secondary: #86868b; /* Override to Apple's secondary text */
    --accent: #3b82f6;
    --accent-dark: #2563eb;
    --accent-gradient: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
    --success-gradient: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
    --card-bg: rgba(255, 255, 255, 0.95);
    
    /* Override ui_utils.py variables */
    --primary: #0071e3; /* Apple blue */
    --primary-dark: #0077ed;
    --primary-light: #f5f5f7;
    --dark-bg: #ffffff;
    --light-bg: #ffffff;
    --border: #d2d2d7;
}
/* Story Mode: Clean White Background - Apple Style */
.stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background: #ffffff !important; /* Pure white background */
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif !important;
    color: #1d1d1f !important; /* Apple's dark text color */
}

[data-testid="stHeader"] {
    background: transparent !important;
}

/* Hide Streamlit Elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stSidebar"] {display: none;}

/* Apple-Style Typography */
h1, h2, h3 {
    text-align: center !important;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', sans-serif !important;
    color: #1d1d1f !important; /* Apple's primary text color */
    font-weight: 600 !important;
    letter-spacing: -0.022em !important; /* Apple's tight letter spacing */
}

h1 {
    font-size: 3rem !important;
    font-weight: 700 !important;
    line-height: 1.05 !important;
}

h2 {
    font-size: 2.25rem !important;
    font-weight: 600 !important;
    line-height: 1.1 !important;
    color: #1d1d1f !important;
}

h3 {
    font-size: 1.75rem !important;
    font-weight: 600 !important;
    line-height: 1.2 !important;
}

p {
    font-size: 1.0625rem !important; /* 17px - Apple's body text size */
    line-height: 1.47059 !important; /* Apple's line height ratio */
    color: #86868b !important; /* Apple's secondary text color */
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
    font-weight: 400 !important;
}

/* Container - Apple Style */
.block-container {
    max-width: 1200px !important; /* Apple's content width */
    padding-top: 2rem !important;
    padding-bottom: 5rem !important;
    background: #ffffff !important;
}


/* Apple-Style Hero Section */
.hero-box {
    text-align: center;
    padding: 3rem 1.5rem 4rem;
    margin: 2rem auto 3rem;
    max-width: 800px;
    position: relative;
    background: #ffffff;
}

.hero-subtitle {
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
    font-weight: 400 !important;
    color: #86868b !important; /* Apple's secondary text color */
    letter-spacing: -0.022em !important;
    font-size: 1.3125rem !important; /* 21px - Apple's large body text */
    margin-top: 1rem !important;
    line-height: 1.47059 !important; /* Apple's line height */
}



/* ULTRA PREMIUM BUTTON DESIGN - GLASSMORPHISM & NEON */
/* Apple-Style Buttons */
div.stButton > button {
    width: 100%;
    position: relative !important;
    overflow: hidden !important;
    
    /* Apple Button Style */
    background: #0071e3 !important; /* Apple's blue */
    border: none !important;
    border-radius: 980px !important; /* Apple's pill shape */
    
    padding: 1rem 2rem !important;
    
    /* Apple Typography - WHITE TEXT */
    color: #ffffff !important;
    font-size: 1.0625rem !important; /* 17px */
    font-weight: 400 !important;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
    letter-spacing: -0.022em !important;
    text-shadow: none !important;
    
    /* Apple Shadow */
    box-shadow: 0 4px 14px rgba(0, 113, 227, 0.39) !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
}

/* Remove gradient border effect */

/* Apple Button Hover */
div.stButton > button:hover {
    background: #0077ed !important;
    box-shadow: 0 4px 14px rgba(0, 119, 237, 0.5) !important;
    color: #ffffff !important; /* Keep white text on hover */
    transform: none !important; /* NO MOVEMENT ON HOVER */
}

/* OVERRIDE ALL BUTTON HOVER TRANSFORMS - NO MOVEMENT */
div.stButton > button:hover,
button:hover,
[role="button"]:hover,
div[data-testid="column"] button:hover,
div.stDownloadButton button:hover {
    transform: none !important; /* Force no transform on ALL buttons */
}

/* Apple Button Active */
div.stButton > button:active {
    background: #006edb !important;
    box-shadow: 0 2px 8px rgba(0, 110, 219, 0.4) !important;
    color: #ffffff !important; /* Keep white text when active */
}

/* Button Text Styling - FORCE WHITE */
div.stButton > button p {
    margin: 0 !important;
    font-weight: 400 !important;
    transform: none !important;
    color: #ffffff !important; /* Force white text */
}

div.stButton > button span {
    color: #ffffff !important; /* Force white text */
}

div.stButton > button div {
    color: #ffffff !important; /* Force white text */
}

/* Explicit Download Button Styling - Match Primary Button */
div.stDownloadButton > button {
    width: 100%;
    position: relative !important;
    overflow: hidden !important;
    background: #0071e3 !important; /* Apple's blue */
    border: none !important;
    border-radius: 980px !important; /* Apple's pill shape */
    padding: 1rem 2rem !important;
    color: #ffffff !important;
    font-size: 1.0625rem !important;
    font-weight: 400 !important;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
    box-shadow: 0 4px 14px rgba(0, 113, 227, 0.39) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

div.stDownloadButton > button:hover {
    background: #0077ed !important;
    color: #ffffff !important;
}

div.stDownloadButton > button p,
div.stDownloadButton > button span {
    color: #ffffff !important;
}


/* Apple-Style Cards */
.info-card {
    background: #f5f5f7 !important; /* Apple's light gray background */
    border: none !important;
    border-radius: 18px !important; /* Apple's rounded corners */
    padding: 2.5rem 2rem !important;
    box-shadow: none !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    position: relative !important;
    overflow: hidden !important;
}

.info-card:hover {
    transform: none !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
    background: #f0f0f2 !important;
}

/* OVERRIDE ALL CARD HOVER TRANSFORMS - NO MOVEMENT */
.info-card:hover,
[data-testid="metric-container"]:hover,
.metric-card:hover,
.scenario-card:hover,
.overview-card:hover {
    transform: none !important; /* Force no transform on ALL cards */
}

.info-card h4 {
    text-align: left !important;
    color: #1d1d1f !important;
    font-size: 1.5rem !important;
    font-weight: 600 !important;
    letter-spacing: -0.022em !important;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif !important;
    margin-bottom: 0.5rem !important;
    line-height: 1.2 !important;
}

.info-card p,
.info-card strong,
.info-card span,
.info-card div {
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
    color: #86868b !important;
    font-size: 1.0625rem !important;
    line-height: 1.47059 !important;
}

.metric-value {
    font-size: 3.5rem !important;
    font-weight: 700 !important;
    color: #1d1d1f !important;
    margin: 1rem 0 !important;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif !important;
    letter-spacing: -0.022em !important;
    line-height: 1.05 !important;
}

.metric-label {
    color: #86868b !important;
    font-size: 1.0625rem !important;
    font-weight: 400 !important;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
    line-height: 1.47059 !important;
}

/* Apple-Style Inputs */
div[data-baseweb="select"] > div, 
div[data-baseweb="input"] > div,
div[data-baseweb="base-input"],
input {
    background-color: #f5f5f7 !important;
    color: #1d1d1f !important;
    border: 1px solid #d2d2d7 !important;
    border-radius: 8px !important;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
    font-size: 1.0625rem !important;
    box-shadow: none !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    padding: 0.75rem 1rem !important;
}

div[data-baseweb="select"] > div, 
div[data-baseweb="input"] > div:hover,
input:hover {
    border-color: #0071e3 !important;
}

div[data-baseweb="select"] > div:focus-within,
input:focus {
    border-color: #0071e3 !important;
    box-shadow: 0 0 0 3px rgba(0, 113, 227, 0.1) !important;
}

/* Apple-Style Selectbox */
div[data-baseweb="select"] > div:first-child {
    background-color: #f5f5f7 !important;
    border: 1px solid #d2d2d7 !important;
    border-radius: 8px !important;
    padding: 0.75rem 1rem !important;
    box-shadow: none !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

div[data-baseweb="select"] > div:first-child:hover {
    border-color: #0071e3 !important;
}

/* SELECTED VALUE DISPLAY - FORCE DARK TEXT */
div[data-baseweb="select"] > div:first-child,
div[data-baseweb="select"] > div:first-child *,
div[data-baseweb="select"] > div:first-child span,
div[data-baseweb="select"] > div:first-child div,
div[data-baseweb="select"] > div:first-child p,
div[data-baseweb="select"] [role="button"],
div[data-baseweb="select"] [role="button"] *,
div[data-baseweb="select"] [role="button"] span,
div[data-baseweb="select"] [role="button"] div,
div[data-baseweb="select"] [role="button"] p {
    color: #1d1d1f !important; /* Force dark text for selected value display */
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
    font-size: 1.0625rem !important;
}

/* Apple-Style Selectbox Text - DARK TEXT */
div[data-baseweb="select"] span, 
div[data-baseweb="select"] div,
[data-baseweb="menu"] div,
[data-baseweb="menu"] span {
    color: #1d1d1f !important; /* Dark text for readability */
    font-size: 1.0625rem !important;
    font-weight: 400 !important;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
}

/* COMPREHENSIVE DROPDOWN TEXT FIXES - FORCE DARK TEXT EVERYWHERE */
.stSelectbox div[data-baseweb="select"] *,
.stSelectbox [role="button"] *,
.stSelectbox [role="button"] span,
.stSelectbox [role="button"] div,
.stSelectbox [role="button"] p,
div[data-baseweb="select"] [role="button"] *,
div[data-baseweb="select"] [role="button"] span,
div[data-baseweb="select"] [role="button"] div,
div[data-baseweb="select"] [role="button"] p,
div[data-baseweb="select"] > div *,
div[data-baseweb="select"] > div span,
div[data-baseweb="select"] > div div,
div[data-baseweb="select"] > div p {
    color: #1d1d1f !important; /* Force dark text for ALL selectbox elements */
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
}

/* ULTRA-SPECIFIC DROPDOWN OPTION OVERRIDES */
[data-baseweb="popover"] [role="option"],
[data-baseweb="popover"] [role="option"] *,
[data-baseweb="popover"] [role="option"] span,
[data-baseweb="popover"] [role="option"] div,
[data-baseweb="popover"] [role="option"] p,
[role="listbox"] [role="option"],
[role="listbox"] [role="option"] *,
[role="listbox"] [role="option"] span,
[role="listbox"] [role="option"] div,
[role="listbox"] [role="option"] p,
div[data-baseweb="menu"] [role="option"],
div[data-baseweb="menu"] [role="option"] *,
div[data-baseweb="menu"] [role="option"] span,
div[data-baseweb="menu"] [role="option"] div,
div[data-baseweb="menu"] [role="option"] p {
    color: #1d1d1f !important; /* FORCE DARK TEXT FOR ALL DROPDOWN OPTIONS */
    background-color: transparent !important;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
}

/* HOVER AND SELECTED STATES */
[role="option"]:hover,
[role="option"]:hover *,
[role="option"]:hover span,
[role="option"]:hover div,
[role="option"]:hover p,
[role="option"][aria-selected="true"],
[role="option"][aria-selected="true"] *,
[role="option"][aria-selected="true"] span,
[role="option"][aria-selected="true"] div,
[role="option"][aria-selected="true"] p {
    color: #1d1d1f !important; /* KEEP DARK TEXT ON HOVER/SELECTED */
    background-color: #f5f5f7 !important;
}

/* Apple-Style Dropdown Menu */
div[data-baseweb="popover"],
div[data-baseweb="menu"] {
    background-color: #ffffff !important;
    border: 1px solid #d2d2d7 !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15) !important;
}

div[data-baseweb="option"] {
    background-color: transparent !important;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
    color: #1d1d1f !important; /* Dark text for options */
}

/* Force dark text for ALL dropdown option elements */
div[data-baseweb="option"] *,
div[data-baseweb="option"] span,
div[data-baseweb="option"] div,
div[data-baseweb="option"] p,
[data-baseweb="menu"] div *,
[data-baseweb="menu"] span *,
[data-baseweb="menu"] div div,
[data-baseweb="menu"] div span {
    color: #1d1d1f !important; /* Force dark text for ALL option elements */
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
}

div[data-baseweb="option"]:hover,
div[data-baseweb="option"][aria-selected="true"] {
    background-color: #f5f5f7 !important;
    font-weight: 400 !important;
    color: #1d1d1f !important; /* Keep dark text on hover */
}

/* Force dark text on hover/selected states too */
div[data-baseweb="option"]:hover *,
div[data-baseweb="option"][aria-selected="true"] *,
div[data-baseweb="option"]:hover span,
div[data-baseweb="option"][aria-selected="true"] span,
div[data-baseweb="option"]:hover div,
div[data-baseweb="option"][aria-selected="true"] div {
    color: #1d1d1f !important; /* Force dark text on hover/selected */
}

/* Apple-Style Labels */
.stSelectbox label p,
.stTextInput label p,
.stDateInput label p {
    font-size: 1.0625rem !important;
    font-weight: 600 !important;
    color: #1d1d1f !important;
    margin-bottom: 0.5rem !important;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
}

/* Expander - Stable Premium Glassmorphism Style */
.streamlit-expanderHeader,
[data-testid="stExpander"] > div:first-child,
[data-testid="stExpander"] summary,
[data-testid="stExpander"] [data-testid="stExpanderToggleIcon"] {
    /* Glassmorphism Background */
    background: rgba(59, 130, 246, 0.1) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
    
    color: #1e40af !important;
    border: 1px solid rgba(59, 130, 246, 0.2) !important;
    border-radius: 16px !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    padding: 1.2rem 1.5rem !important;
    
    box-shadow: 
        0 4px 16px rgba(59, 130, 246, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
    
    /* NO TRANSFORM - STABLE */
    transform: none !important;
    transition: background 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease !important;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
}

[data-testid="stExpander"] summary {
    display: flex !important;
    align-items: center !important;
    gap: 0.5rem !important;
    cursor: pointer !important;
}

[data-testid="stExpander"] summary:hover {
    transform: none !important;
    background: rgba(59, 130, 246, 0.15) !important;
    box-shadow: 
        0 6px 20px rgba(59, 130, 246, 0.15),
        inset 0 1px 0 rgba(255, 255, 255, 0.4) !important;
    border-color: rgba(59, 130, 246, 0.3) !important;
}

[data-testid="stExpander"] summary span,
[data-testid="stExpander"] summary p,
.streamlit-expanderHeader span,
.streamlit-expanderHeader p {
    color: #1e40af !important;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
}

[data-testid="stExpander"] svg,
.streamlit-expanderHeader svg {
    fill: #3b82f6 !important;
    color: #3b82f6 !important;
}

/* Hide material icon text artifacts */
[data-testid="stExpander"] [data-testid="stMarkdownContainer"] p:empty,
.streamlit-expanderHeader svg text {
    display: none !important;
}


/* DataFrames - Blue Theme */
[data-testid="stDataFrame"] {
    background-color: white !important;
    color: var(--text-primary) !important;
    border: 2px solid rgba(59, 130, 246, 0.2);
    border-radius: 12px;
}

[data-testid="stDataFrame"] div[role="grid"],
[data-testid="stDataFrame"] div[role="columnheader"] {
    color: var(--text-primary) !important;
    background-color: #eff6ff !important;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
}

/* Plotly Charts */
.js-plotly-plot .plotly .modebar {
    background-color: transparent !important;
}
.js-plotly-plot .plotly .modebar-btn {
    background-color: transparent !important;
}
.js-plotly-plot .plotly .modebar-btn path {
    fill: #1e40af !important;
}
.js-plotly-plot .plotly .modebar-btn:hover path {
    fill: #3b82f6 !important;
}

/* Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeScale {
    from {
        opacity: 0;
        transform: scale(0.95);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

/* Buton animasyonları kaldırıldı - hemen görünür */

.info-card {
    animation: fadeInUp 0.7s ease-out forwards;
    opacity: 0;
    animation-delay: 0.3s;
}

div[data-testid="stImage"] {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    animation: fadeScale 0.8s ease-out;
}

/* PREMIUM LOADING ANIMATIONS */
.premium-loader {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 3rem 2rem;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 20px;
    border: 1px solid rgba(59, 130, 246, 0.2);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    margin: 2rem auto;
    max-width: 400px;
}

.loader-animation {
    position: relative;
    width: 80px;
    height: 80px;
    margin-bottom: 2rem;
}

/* Spinning Gradient Ring */
.gradient-ring {
    position: absolute;
    width: 80px;
    height: 80px;
    border: 4px solid transparent;
    border-radius: 50%;
    background: linear-gradient(45deg, #3b82f6, #8b5cf6, #06b6d4, #10b981) border-box;
    background-clip: border-box;
    animation: spin 2s linear infinite;
}

.gradient-ring::before {
    content: '';
    position: absolute;
    top: -4px;
    left: -4px;
    right: -4px;
    bottom: -4px;
    background: linear-gradient(45deg, #3b82f6, #8b5cf6, #06b6d4, #10b981);
    border-radius: 50%;
    z-index: -1;
    animation: spin 2s linear infinite;
}

.gradient-ring::after {
    content: '';
    position: absolute;
    top: 4px;
    left: 4px;
    right: 4px;
    bottom: 4px;
    background: white;
    border-radius: 50%;
    z-index: 1;
}

/* Pulsing Dots */
.pulse-dots {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    display: flex;
    gap: 8px;
}

.pulse-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: linear-gradient(45deg, #3b82f6, #8b5cf6);
    animation: pulse 1.5s ease-in-out infinite;
}

.pulse-dot:nth-child(2) {
    animation-delay: 0.3s;
}

.pulse-dot:nth-child(3) {
    animation-delay: 0.6s;
}

/* Loading Text */
.loader-text {
    font-size: 1.1rem;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 0.5rem;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.loader-subtext {
    font-size: 0.9rem;
    color: #64748b;
    text-align: center;
    line-height: 1.4;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

/* Progress Bar */
.progress-container {
    width: 100%;
    height: 4px;
    background: rgba(59, 130, 246, 0.1);
    border-radius: 2px;
    margin-top: 1.5rem;
    overflow: hidden;
}

.progress-bar {
    height: 100%;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6, #06b6d4);
    background-size: 200% 100%;
    border-radius: 2px;
    animation: progressFlow 2s ease-in-out infinite;
    width: 70%;
}

/* Keyframe Animations */
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

@keyframes pulse {
    0%, 100% { 
        opacity: 0.3;
        transform: scale(0.8);
    }
    50% { 
        opacity: 1;
        transform: scale(1.2);
    }
}

@keyframes progressFlow {
    0% { 
        background-position: -200% 0;
        opacity: 0.6;
    }
    50% {
        opacity: 1;
    }
    100% { 
        background-position: 200% 0;
        opacity: 0.6;
    }
}

/* Floating Particles */
.loader-particles {
    position: absolute;
    width: 100%;
    height: 100%;
    pointer-events: none;
}

.particle {
    position: absolute;
    width: 4px;
    height: 4px;
    background: linear-gradient(45deg, #3b82f6, #8b5cf6);
    border-radius: 50%;
    opacity: 0.6;
    animation: float 3s ease-in-out infinite;
}

.particle:nth-child(1) { top: 20%; left: 20%; animation-delay: 0s; }
.particle:nth-child(2) { top: 80%; left: 80%; animation-delay: 1s; }
.particle:nth-child(3) { top: 60%; left: 10%; animation-delay: 2s; }
.particle:nth-child(4) { top: 30%; left: 90%; animation-delay: 1.5s; }

@keyframes float {
    0%, 100% { 
        transform: translateY(0px) scale(1);
        opacity: 0.6;
    }
    50% { 
        transform: translateY(-20px) scale(1.2);
        opacity: 1;
    }
}

/* İkinci buton animasyonu da kaldırıldı */

.info-card {
    animation: fadeInUp 0.7s ease-out forwards;
    opacity: 0;
    animation-delay: 0.3s;
}

div[data-testid="stImage"] {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    animation: fadeScale 0.8s ease-out;
}

/* Status widgets */
div[data-testid="stStatusWidget"] {
    background-color: rgba(255, 255, 255, 0.95) !important;
    border: 2px solid rgba(59, 130, 246, 0.2) !important;
    border-radius: 12px !important;
}

/* Success/Info boxes */
.stSuccess {
    background-color: #dbeafe !important;
    color: var(--text-primary) !important;
    border-left: 4px solid var(--accent) !important;
}

/* ===== METRICS - FORCE SF PRO FONT ===== */
[data-testid="stMetricValue"],
[data-testid="stMetricLabel"],
[data-testid="stMetricDelta"],
.stMetric,
[data-testid="stMetric"],
[data-testid="stMetric"] *,
[data-testid="stMetricValue"] *,
[data-testid="stMetricLabel"] *,
[data-testid="stMetricDelta"] * {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Segoe UI', sans-serif !important;
}

[data-testid="stMetricValue"],
[data-testid="stMetricValue"] div,
[data-testid="stMetricValue"] span,
[data-testid="stMetricValue"] p {
    font-size: 2rem !important;
    font-weight: 700 !important;
    color: var(--text-primary) !important;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] div,
[data-testid="stMetricLabel"] span,
[data-testid="stMetricLabel"] p {
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    color: var(--text-secondary) !important;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
}

/* Button text - force WHITE for all buttons */
div.stButton > button,
div.stButton > button span,
div.stButton > button p,
div.stButton > button div,
div[data-testid="column"] button,
div[data-testid="column"] button span,
div[data-testid="column"] button p,
div[data-testid="column"] button div,
div.stDownloadButton button,
div.stDownloadButton button span,
div.stDownloadButton button p,
div.stDownloadButton button div {
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
    color: #ffffff !important; /* Force white text for ALL buttons */
}

/* Checkbox - Premium Style like Performance Insights heading */
[data-testid="stCheckbox"] label,
[data-testid="stCheckbox"] label span,
[data-testid="stCheckbox"] label p {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    color: #0071e3 !important;
    letter-spacing: -0.01em !important;
}

[data-testid="stCheckbox"] > label {
    display: flex !important;
    align-items: center !important;
    gap: 0.5rem !important;
    padding: 0.75rem 1rem !important;
    background: rgba(59, 130, 246, 0.05) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(59, 130, 246, 0.15) !important;
    cursor: pointer !important;
}

[data-testid="stCheckbox"] > label:hover {
    background: rgba(59, 130, 246, 0.1) !important;
    border-color: rgba(59, 130, 246, 0.3) !important;
}

/* Caption text under buttons */
.stCaption, .stCaption p {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    color: var(--text-secondary) !important;
}

/* Info card content */
.info-card p,
.info-card strong,
.info-card span {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
}

/* Download buttons - special styling */
div.stDownloadButton > button,
div.stDownloadButton > button span,
div.stDownloadButton > button p {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    font-weight: 600 !important;
}

/* All button text - comprehensive coverage */
button,
button span,
button p,
button div,
[role="button"],
[role="button"] span,
[role="button"] p {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
}

/* FINAL OVERRIDE - FIXED DROPDOWN VISIBILITY */
/* Target popovers specifically, which may exist outside .stApp */
div[data-baseweb="popover"],
div[data-baseweb="popover"] > div,
div[data-baseweb="popover"] > div > div {
    background-color: #ffffff !important;
    color: #1d1d1f !important;
}

/* Target the options list and items directly */
div[data-baseweb="popover"] [role="listbox"],
div[data-baseweb="popover"] [role="option"] {
    background-color: #ffffff !important;
    color: #1d1d1f !important; /* Forces dark text */
}

/* Target deep elements inside options (spans, divs, paragraphs) */
div[data-baseweb="popover"] [role="option"] *,
div[data-baseweb="popover"] [role="option"] span,
div[data-baseweb="popover"] [role="option"] div,
div[data-baseweb="popover"] [role="option"] p {
    color: #1d1d1f !important;
    background-color: transparent !important; /* Inherit white from parent */
    opacity: 1 !important;
}

/* Hover and Selected States */
div[data-baseweb="popover"] [role="option"]:hover,
div[data-baseweb="popover"] [role="option"][aria-selected="true"] {
    background-color: #f5f5f7 !important; /* Light gray hover */
    color: #0071e3 !important; /* Apple Blue highlight */
}

div[data-baseweb="popover"] [role="option"]:hover *,
div[data-baseweb="popover"] [role="option"][aria-selected="true"] * {
    color: #0071e3 !important;
}

/* NUCLEAR FIX for Selected Option Visibility */
/* Target the container of the selected value */
div[data-baseweb="select"] > div:first-child {
    background-color: #ffffff !important;
    border: 1px solid #d2d2d7 !important;
    color: #000000 !important; /* Pure black */
}

/* Force ALL children text to be black and visible */
div[data-baseweb="select"] > div:first-child * {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    opacity: 1 !important;
    visibility: visible !important;
    font-weight: 500 !important;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
}

/* Exclude the SVG arrow icon from being blacked out if it acts as a mask, 
   but usually filling it black is fine for visibility too */
div[data-baseweb="select"] > div:first-child svg {
    fill: #0071e3 !important; /* Blue arrow */
    color: #0071e3 !important;
}

/* Check for any 'role=button' interference and override it specifically for selectbox */
div[data-baseweb="select"] [role="button"],
div[data-baseweb="select"] [role="button"] *,
div[data-baseweb="select"] [role="button"] span,
div[data-baseweb="select"] [role="button"] div {
     color: #000000 !important;
}

</style>
<script>
// AGGRESSIVE FIX for selectbox visibility
(function() {
    function forceSelectboxVisibility() {
        // Target ALL possible selectbox text elements
        const selectors = [
            '[data-baseweb="select"] *',
            '[data-baseweb="select"] span',
            '[data-baseweb="select"] div',
            '[data-baseweb="select"] p',
            '.stSelectbox *',
            '.stSelectbox span',
            '.stSelectbox div',
            '.stSelectbox p',
            '[role="button"] *',
            '[role="button"] span',
            '[role="button"] div',
            '[role="option"] *',
            '[role="option"] span',
            '[role="option"] div'
        ];
        
        selectors.forEach(selector => {
            try {
                const elements = document.querySelectorAll(selector);
                elements.forEach(el => {
                    // Force dark text with multiple methods
                    el.style.color = '#1d1d1f';
                    el.style.setProperty('color', '#1d1d1f', 'important');
                    el.style.opacity = '1';
                    el.style.setProperty('opacity', '1', 'important');
                    el.style.visibility = 'visible';
                    el.style.setProperty('visibility', 'visible', 'important');
                    
                    // Remove any conflicting styles
                    el.style.removeProperty('-webkit-text-fill-color');
                    el.style.removeProperty('background-clip');
                    el.style.removeProperty('-webkit-background-clip');
                });
            } catch(e) {}
        });
    }
    
    // Run immediately and repeatedly
    forceSelectboxVisibility();
    setTimeout(forceSelectboxVisibility, 100);
    setTimeout(forceSelectboxVisibility, 300);
    setTimeout(forceSelectboxVisibility, 500);
    setTimeout(forceSelectboxVisibility, 1000);
    
    // Watch for changes
    const observer = new MutationObserver(forceSelectboxVisibility);
    observer.observe(document.body, { 
        childList: true, 
        subtree: true,
        attributes: true,
        attributeFilter: ['style', 'class']
    });
    
    // Keep running periodically
    setInterval(forceSelectboxVisibility, 300);
})();
</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
""", unsafe_allow_html=True)
# Session State Initialization
if 'data_mode' not in st.session_state:
    st.session_state.data_mode = None  # 'open_data' or 'upload'
if 'language' not in st.session_state:
    st.session_state.language = 'en'  # Default language

def reset_app():
    for key in ['df', 'analysis', 'data_mode']:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

def t(key):
    """Translation helper function"""
    return translations.get_text(key, st.session_state.language)

# --- HEADER / HERO SECTION ---
def render_hero():
    # Language selector at top right
    col_lang1, col_lang2, col_lang3 = st.columns([4, 1, 1])
    with col_lang3:
        available_langs = translations.get_available_languages()
        selected_lang = st.radio(
            "Language",
            options=list(available_langs.keys()),
            format_func=lambda x: available_langs[x],
            index=list(available_langs.keys()).index(st.session_state.language),
            key="language_selector",
            label_visibility="collapsed",
            horizontal=True
        )
        if selected_lang != st.session_state.language:
            st.session_state.language = selected_lang
            st.rerun()
    
    # Logo'yu tam ortaya almak için daha geniş orta kolon
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        try:
            st.image("assets/octogreen-logo.png", width=400)
        except:
            st.markdown(f"<h1 style='text-align: center;'>{t('app_title')}</h1>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style="text-align: center; margin-top: 0.5rem; margin-bottom: 2rem; opacity: 0.8;">
            <p style="font-size: 0.8rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 600; margin-bottom: 10px;">
                Thanks for help
            </p>
            <div style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
                <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" height="25" style="border-radius: 4px;">
                <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" height="25" style="border-radius: 4px;">
                <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" height="25" style="border-radius: 4px;">
                <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white" height="25" style="border-radius: 4px;">
            </div>
        </div>

        <div class="hero-box">
            <p class="hero-subtitle">{t('hero_subtitle')}<br><span style="font-size: 0.95rem; color: #64748b;">{t('hero_description')}</span></p>
        </div>
    """, unsafe_allow_html=True)

# --- MAIN SELECTION SCREEN ---
# --- MAIN SELECTION SCREEN ---
def render_selection_screen():
    # Page Transition Animations
    st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .main-menu-container {
        animation: fadeIn 0.5s ease-out forwards;
    }
    .sub-page-container {
        animation: fadeIn 0.4s ease-out forwards;
    }
    .custom-caption {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
        color: #86868b !important; /* Apple's secondary gray for readability on white background */
        text-align: center !important;
        font-size: 0.9rem !important;
        margin-top: -10px !important;
        font-weight: 500 !important;
        line-height: 1.4 !important;
        opacity: 0.9;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # 1. MAIN MENU STATE (No selection yet)
    if st.session_state.data_mode is None:
        st.markdown('<div class="main-menu-container">', unsafe_allow_html=True)
        render_hero()
        
        # Centered Navigation Grid
        col_space_l, col1, col2, col_space_r = st.columns([1, 2, 2, 1], gap="large")
        
        with col1:
             # Added Globe Icon directly to button text
             if st.button(f"{t('browse_open_data')}", key="btn_open_data", width="stretch"):
                st.session_state.data_mode = 'open_data'
                st.rerun()
             # Updated caption to custom centered HTML
             st.markdown(f'<p class="custom-caption">{t("open_data_desc")}</p>', unsafe_allow_html=True)

        with col2:
             # Added Cloud Icon directly to button text
             if st.button(f"{t('upload_your_own')}", key="btn_upload", width="stretch"):
                st.session_state.data_mode = 'upload'
                st.rerun()
             # Updated caption to custom centered HTML
             st.markdown(f'<p class="custom-caption">{t("upload_desc")}</p>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

    # 2. OPEN DATA PAGE
    elif st.session_state.data_mode == 'open_data':
        st.markdown('<div class="sub-page-container">', unsafe_allow_html=True)
        
        # Header with Back Button
        c_back, c_title = st.columns([0.5, 4])
        with c_back:
            if st.button("←", key="back_btn_open", help="Back to Menu"):
                st.session_state.data_mode = None
                st.rerun()
        with c_title:
             st.markdown(f"<h2 style='margin:0; padding-top:5px;'>{t('select_dataset')}</h2>", unsafe_allow_html=True)
        
        st.markdown("<hr style='margin-top:0.5rem; margin-bottom:2rem; opacity:0.3;'>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_opts, col_detais = st.columns([1.2, 0.8], gap="large")
        
        with col_opts:
            # Replaced Dropdown with Radio for better visibility
            source = st.radio(t("choose_source"), [
                "UK National Grid - Carbon Intensity (~96 records)",
                "WRI - Global Power Plants (~96 records)",
                "World Bank - Energy & Carbon (~500 records)",
                "Eurostat - EU Energy (~1K records)",
                "US EIA - Electricity Stats (~1K records)",
                "IEA - Global Energy Data (~5K records)",
                "EPIAS Turkey (Real-time)",
                "UCI Household (2M+ records)"
            ], index=0)
            

            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Action Area
            if "UK National Grid" in source:
                if st.button(t("fetch_uk_carbon"), key="dl_uk", width="stretch"):
                    with st.spinner("Fetching UK Carbon Data - Connecting to National Grid API..."):
                        df = open_data.fetch_uk_carbon_intensity()
                    
                    if df is not None:
                        st.session_state.df = df
                        st.rerun()
                    else:
                        st.error("Failed to fetch UK data")

            elif "WRI" in source:
                if st.button(t("fetch_power_plants"), key="dl_wri", width="stretch"):
                    with st.spinner("Fetching Global Power Plants - Accessing World Resources Institute database..."):
                        df = open_data.fetch_global_power_plants()
                    
                    if df is not None:
                        st.session_state.df = df
                        st.rerun()
                    else:
                        st.error("Failed to fetch Power Plant data")
                            
            elif "World Bank" in source:
                 if st.button(t("fetch_world_bank"), key="dl_wb", width="stretch"):
                    with st.spinner(t("accessing_wb") + " - Retrieving global energy indicators..."):
                        energy_df = open_data.fetch_world_bank_energy()
                    
                    if energy_df is not None:
                        df = energy_df.copy()
                        df["timestamp"] = pd.to_datetime(df["year"], format="%Y")
                        df["device_id"] = df["country"]
                        df["consumption_kWh"] = df["consumption_kwh_per_capita"]
                        st.session_state.df = df[["timestamp", "device_id", "consumption_kWh"]].dropna()
                        st.rerun()
                            
            elif "Eurostat" in source:
                if st.button(t("fetch_eu_data"), key="dl_eurostat", width="stretch"):
                    with st.spinner("🇪🇺 " + t("accessing_eurostat") + " - Connecting to European Union statistics..."):
                        df = open_data.fetch_eurostat_energy()
                    
                    if df is not None:
                        st.session_state.df = df
                        st.rerun()
                    else:
                        st.error(t("failed_eurostat"))
            
            elif "US EIA" in source:
                if st.button(t("fetch_us_data"), key="dl_eia", width="stretch"):
                    with st.spinner("🇺🇸 " + t("accessing_eia") + " - Accessing US Energy Information Administration..."):
                        df = open_data.fetch_us_eia_electricity()
                    
                    if df is not None:
                        st.session_state.df = df
                        st.rerun()
                    else:
                        st.error(t("failed_eia"))
            
            elif "IEA" in source:
                if st.button(t("fetch_iea"), key="dl_iea", width="stretch"):
                    with st.spinner("⚡ " + t("accessing_iea") + " - Connecting to International Energy Agency..."):
                        df = open_data.fetch_iea_global_energy()
                    
                    if df is not None:
                        st.session_state.df = df
                        st.rerun()
                    else:
                        st.error(t("failed_iea"))

            elif "EPIAS Turkey" in source:
                c1, c2 = st.columns(2)
                with c1:
                    start = st.date_input(t("start_date"), datetime.now() - timedelta(days=7))
                with c2:
                    end = st.date_input(t("end_date"), datetime.now())
                
                if st.button(t("fetch_live_data"), key="dl_epias", width="stretch"):
                    with st.spinner("🇹🇷 " + t("fetching_live") + " - Connecting to Turkey Energy Exchange..."):
                        df = open_data.fetch_epias_data(start, end)
                    
                    if df is not None:
                        st.session_state.df = df
                        st.rerun()
                    else:
                        st.error(t("failed_epias"))

            elif "UCI Household" in source:
                if st.button(t("download_analyze"), key="dl_uci", width="stretch"):
                    # Multi-step loading with progress
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    # Step 1: Connecting
                    status_text.text("🔗 " + t("connecting") + " - Establishing secure connection to UCI repository...")
                    progress_bar.progress(25)
                    time.sleep(1)
                    
                    # Step 2: Downloading
                    status_text.text("⬇️ " + t("downloading") + " - Downloading 2M+ household power consumption records...")
                    progress_bar.progress(50)
                    st.session_state.df = open_data.fetch_kaggle_household()
                    progress_bar.progress(75)
                    time.sleep(0.5)
                    
                    # Step 3: Processing
                    status_text.text("⚙️ " + t("running_analysis") + " - Preparing data for advanced analytics...")
                    progress_bar.progress(100)
                    time.sleep(1)
                    
                    # Clear loading elements
                    progress_bar.empty()
                    status_text.empty()
                    st.success("✅ " + t("ready"))
                    time.sleep(0.5)
                    st.rerun()

        with col_detais:
            if "Manual Data" in source:
                st.markdown(f"""
                <div class="info-card">
                    <h4>Manual Entry</h4>
                    <div class="metric-value">~168</div>
                    <p>Estimated records</p>
                    <div style="margin-top:1rem; border-top:2px solid rgba(59, 130, 246, 0.2); padding-top:1rem;">
                        <p style="font-size:0.9rem; color:#64748b;"><strong>Contains</strong><br>Monthly bill estimates, device-based calculations</p>
                        <p style="font-size:0.9rem; color:#64748b;"><strong>Best for</strong><br>Quick prototyping, small-scale analysis</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif "Test Data CSV" in source:
                st.markdown(f"""
                <div class="info-card">
                    <h4>Test Dataset</h4>
                    <div class="metric-value">8</div>
                    <p>Sample records</p>
                    <div style="margin-top:1rem; border-top:2px solid rgba(59, 130, 246, 0.2); padding-top:1rem;">
                        <p style="font-size:0.9rem; color:#64748b;"><strong>Contains</strong><br>Sample IoT device data for testing</p>
                        <p style="font-size:0.9rem; color:#64748b;"><strong>Best for</strong><br>Testing app functionality, demos</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif "UK National Grid" in source:
                st.markdown(f"""
                <div class="info-card">
                    <h4>UK Carbon Grid</h4>
                    <div class="metric-value">~96</div>
                    <p>Hourly records</p>
                    <div style="margin-top:1rem; border-top:2px solid rgba(59, 130, 246, 0.2); padding-top:1rem;">
                        <p style="font-size:0.9rem; color:#64748b;"><strong>Contains</strong><br>Real-time carbon intensity data (gCO2/kWh)</p>
                        <p style="font-size:0.9rem; color:#64748b;"><strong>Best for</strong><br>Carbon footprint analysis, grid monitoring</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif "WRI" in source:
                st.markdown(f"""
                <div class="info-card">
                    <h4>Global Power Plants</h4>
                    <div class="metric-value">~96</div>
                    <p>Plant records</p>
                    <div style="margin-top:1rem; border-top:2px solid rgba(59, 130, 246, 0.2); padding-top:1rem;">
                        <p style="font-size:0.9rem; color:#64748b;"><strong>Contains</strong><br>Solar & wind power generation by country</p>
                        <p style="font-size:0.9rem; color:#64748b;"><strong>Best for</strong><br>Renewable energy analysis, country comparisons</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif "World Bank" in source:
                 st.markdown(f"""
                <div class="info-card">
                    <h4>{t('global_indicators')}</h4>
                    <div class="metric-value">~500</div>
                    <p>{t('countries_regions')}</p>
                    <div style="margin-top:1rem; border-top:2px solid rgba(59, 130, 246, 0.2); padding-top:1rem;">
                        <p style="font-size:0.9rem; color:#64748b;"><strong>{t('contains')}</strong><br>{t('wb_contains')}</p>
                        <p style="font-size:0.9rem; color:#64748b;"><strong>{t('best_for')}</strong><br>{t('wb_best')}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif "Eurostat" in source:
                st.markdown(f"""
                <div class="info-card">
                    <h4>{t('eu_stats')}</h4>
                    <div class="metric-value">~1K</div>
                    <p>EU records</p>
                    <div style="margin-top:1rem; border-top:2px solid rgba(59, 130, 246, 0.2); padding-top:1rem;">
                        <p style="font-size:0.9rem; color:#64748b;"><strong>{t('contains')}</strong><br>{t('eurostat_contains')}</p>
                        <p style="font-size:0.9rem; color:#64748b;"><strong>{t('best_for')}</strong><br>{t('eurostat_best')}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif "US EIA" in source:
                st.markdown(f"""
                <div class="info-card">
                    <h4>{t('us_energy_authority')}</h4>
                    <div class="metric-value">~1K</div>
                    <p>{t('production_records')}</p>
                    <div style="margin-top:1rem; border-top:2px solid rgba(59, 130, 246, 0.2); padding-top:1rem;">
                        <p style="font-size:0.9rem; color:#64748b;"><strong>{t('contains')}</strong><br>{t('eia_contains')}</p>
                        <p style="font-size:0.9rem; color:#64748b;"><strong>{t('best_for')}</strong><br>{t('eia_best')}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif "IEA" in source:
                st.markdown(f"""
                <div class="info-card">
                    <h4>{t('iea_database')}</h4>
                    <div class="metric-value">~5K</div>
                    <p>{t('global_records')}</p>
                    <div style="margin-top:1rem; border-top:2px solid rgba(59, 130, 246, 0.2); padding-top:1rem;">
                        <p style="font-size:0.9rem; color:#64748b;"><strong>{t('contains')}</strong><br>{t('iea_contains')}</p>
                        <p style="font-size:0.9rem; color:#64748b;"><strong>{t('best_for')}</strong><br>{t('iea_best')}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif "EPIAS Turkey" in source:
                 st.markdown(f"""
                <div class="info-card">
                    <h4>{t('real_time_feed')}</h4>
                    <div class="metric-value">Live</div>
                    <p>Energy Exchange Istanbul</p>
                    <div style="margin-top:1rem; border-top:2px solid rgba(59, 130, 246, 0.2); padding-top:1rem;">
                        <p style="font-size:0.9rem; color:#64748b;"><strong>{t('contains')}</strong><br>{t('epias_contains')}</p>
                        <p style="font-size:0.9rem; color:#64748b;"><strong>{t('best_for')}</strong><br>{t('epias_best')}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif "UCI Household" in source:
                st.markdown(f"""
                <div class="info-card">
                    <h4>{t('dataset_snapshot')}</h4>
                    <div class="metric-value">2M+</div>
                    <p>{t('individual_records')}</p>
                    <div style="margin-top:1rem; border-top:2px solid rgba(59, 130, 246, 0.2); padding-top:1rem;">
                        <p style="font-size:0.9rem; color:#64748b;"><strong>{t('contains')}</strong><br>{t('uci_contains')}</p>
                        <p style="font-size:0.9rem; color:#64748b;"><strong>{t('best_for')}</strong><br>{t('uci_best')}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)


    # 3. UPLOAD PAGE
    elif st.session_state.data_mode == 'upload':
        st.markdown('<div class="sub-page-container">', unsafe_allow_html=True)
        
        # Header with Back Button
        c_back, c_title = st.columns([0.5, 4])
        with c_back:
            if st.button("←", key="back_btn_up", help="Back to Menu"):
                st.session_state.data_mode = None
                st.rerun()
        with c_title:
             st.markdown(f"<h2 style='margin:0; padding-top:5px;'>{t('upload_data')}</h2>", unsafe_allow_html=True)
             
        st.markdown("<hr style='margin-top:0.5rem; margin-bottom:2rem; opacity:0.3;'>", unsafe_allow_html=True)
        
        uploaded = st.file_uploader("Upload CSV", type=["csv"], label_visibility="collapsed")
        
        if uploaded:
            st.session_state.df = pd.read_csv(uploaded)
            st.success(t("file_uploaded"))
            time.sleep(1)
            st.rerun()
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(
            t("download_template"),
            "timestamp,device_id,consumption_kWh\n2026-01-01 00:00:00,Device_1,0.45\n",
            file_name="template.csv",
        )

# --- DASHBOARD (DATA LOADED) ---
def render_dashboard():
    df = st.session_state.df 
    
    # Custom CSS for Navbar alignment and Styling
    st.markdown("""
        <style>
        /* Top Bar Container Style */
        div[data-testid="stHorizontalBlock"]:first-of-type {
            align-items: center;
            padding-bottom: 1rem;
        }
        
        /* Selectbox Styling */
        div[data-testid="stSelectbox"] > div > div {
            min-height: 40px !important;
            height: 40px !important;
            border-radius: 8px !important;
            border-color: #e2e8f0 !important;
            background-color: #ffffff !important;
        }
        
        /* GENERAL BUTTON STYLING - STABLE MINI BUTTONS */
        div[data-testid="column"] button {
            height: 40px !important;
            min-height: 40px !important;
            max-height: 40px !important;
            padding: 0px 16px !important;
            font-size: 0.9rem !important;
            border-radius: 12px !important;
            
            /* Mini Apple Style */
            background: #0071e3 !important;
            border: none !important;
            color: #ffffff !important; /* White text */
            
            box-shadow: 0 2px 8px rgba(0, 113, 227, 0.3) !important;
            
            font-weight: 400 !important;
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
            
            white-space: nowrap !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            width: 100% !important;
            
            /* NO TRANSFORM - STABLE */
            transform: none !important;
            transition: background 0.2s ease, box-shadow 0.2s ease !important;
        }

        /* Mini Button Hover - NO MOVEMENT */
        div[data-testid="column"] button:hover {
            transform: none !important;
            background: #0077ed !important;
            color: #ffffff !important; /* Keep white text */
            box-shadow: 0 4px 12px rgba(0, 119, 237, 0.4) !important;
        }

        /* Mini Button Active - NO MOVEMENT */
        div[data-testid="column"] button:active {
            transform: none !important;
            background: #006edb !important;
            color: #ffffff !important; /* Keep white text */
        }

        /* Force white text in mini buttons */
        div[data-testid="column"] button p,
        div[data-testid="column"] button span,
        div[data-testid="column"] button div {
            color: #ffffff !important;
        }

        /* RESET CONTENT STYLES INSIDE BUTTON */
        div[data-testid="column"] button p {
            margin: 0 !important;
            padding: 0 !important;
            line-height: 1 !important;
            font-weight: 500 !important;
        }

        div[data-testid="column"] button div {
            margin: 0 !important;
            padding: 0 !important;
            line-height: 1 !important;
        }
        
        /* Remove default margins from button containers */
        div.stButton {
            margin: 0 !important;
            padding: 0 !important;
            height: 40px !important;
            width: 100% !important;
        }
        
        div.stDownloadButton button {
            font-weight: 400 !important;
            /* Download Button - Apple Style */
            background: #0071e3 !important;
            border: none !important;
            border-radius: 8px !important;
            color: #ffffff !important; /* White text */
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
            box-shadow: 0 2px 8px rgba(0, 113, 227, 0.3) !important;
            /* NO TRANSFORM */
            transform: none !important;
            transition: background 0.2s ease, box-shadow 0.2s ease !important;
        }
        
        div.stDownloadButton button:hover {
            transform: none !important;
            background: #0077ed !important;
            color: #ffffff !important; /* Keep white text */
            box-shadow: 0 4px 12px rgba(0, 119, 237, 0.4) !important;
        }

        /* Force white text in download buttons */
        div.stDownloadButton button p,
        div.stDownloadButton button span,
        div.stDownloadButton button div {
            color: #ffffff !important;
        }
        
        /* Logo Alignment */
        div[data-testid="column"]:first-child img {
            margin-top: 4px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Navbar Layout: Logo | Spacer | Language | Mini-Spacer | New Analysis
    # Added explicit spacing between language and button
    c_logo, c_space, c_lang, c_gap, c_reset = st.columns([1.5, 3.4, 2.5, 0.3, 2.3], gap="small")
    
    with c_logo:
        st.image("assets/octogreen-logo.png", width=130)
        
    with c_space:
        pass # Big Spacer
        
    with c_lang:
        available_langs = translations.get_available_languages()
        selected_lang = st.radio(
            "Language",
            options=list(available_langs.keys()),
            format_func=lambda x: available_langs[x],
            index=list(available_langs.keys()).index(st.session_state.language),
            key="dashboard_language_selector",
            label_visibility="collapsed",
            horizontal=True
        )
        if selected_lang != st.session_state.language:
            st.session_state.language = selected_lang
            st.rerun()
            
    with c_gap:
        pass # Small Spacer between lang and button
            
    with c_reset:
        if st.button(f"↻  {t('new_analysis')}", key="btn_new_analysis"):
            reset_app()
    
    st.divider()
    
    # Calculate analysis
    analysis = st.session_state.get('analysis')
    if analysis is None:
        with st.spinner("🤖 " + t("processing_analytics") + " - Running advanced AI analysis on your data..."):
            analysis = ai_analysis.analyze(df)
        st.session_state.analysis = analysis

    # Modern Dataset Overview
    st.markdown(f"""
    <div style='text-align: center; margin-top: 2rem; margin-bottom: 2rem;'>
        <h3 style='font-size: 1.4rem; font-weight: 600; color: #1e293b; letter-spacing: -0.01em;'>{t('dataset_overview')}</h3>
        <div style='height: 3px; width: 60px; background: linear-gradient(90deg, #3b82f6, #06b6d4); margin: 0.5rem auto 0; border-radius: 2px;'></div>
    </div>
    
    <style>
    .overview-card {{
        background: #f5f5f7;
        border: none;
        border-radius: 18px;
        padding: 1.5rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        box-shadow: none;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }}
    .overview-card:hover {{
        transform: none !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        background: #f0f0f2;
    }}
    .overview-icon {{
        width: 48px;
        height: 48px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.25rem;
        flex-shrink: 0;
    }}
    .overview-label {{
        font-size: 0.8125rem;
        color: #86868b;
        font-weight: 400;
        margin-bottom: 0.2rem;
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif;
        line-height: 1.47059;
    }}
    .overview-value {{
        font-size: 1.5rem;
        font-weight: 600;
        color: #1d1d1f;
        line-height: 1.2;
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif;
        letter-spacing: -0.022em;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    m1, m2, m3 = st.columns(3, gap="medium")
    
    with m1:
        st.markdown(f"""
        <div class='overview-card'>
            <div class='overview-icon' style='background: #eff6ff; color: #3b82f6;'>
                <i class="fa-solid fa-server"></i>
            </div>
            <div>
                <div class='overview-label'>{t("total_records")}</div>
                <div class='overview-value'>{len(df):,}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with m2:
        timeline_val = t("time_series_data") if 'timestamp' in df.columns else t("tabular")
        timeline_icon = "fa-clock" if 'timestamp' in df.columns else "fa-table"
        st.markdown(f"""
        <div class='overview-card'>
            <div class='overview-icon' style='background: #f5f3ff; color: #8b5cf6;'>
                <i class="fa-solid {timeline_icon}"></i>
            </div>
            <div>
                <div class='overview-label'>{t("timeline")}</div>
                <div class='overview-value' style='font-size: 1.1rem;'>{timeline_val}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with m3:
        source_count = df['device_id'].nunique() if 'device_id' in df.columns else 1
        st.markdown(f"""
        <div class='overview-card'>
            <div class='overview-icon' style='background: #ecfeff; color: #06b6d4;'>
                <i class="fa-solid fa-bolt"></i>
            </div>
            <div>
                <div class='overview-label'>{t("sources")}</div>
                <div class='overview-value'>{source_count}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Main Content Area - Single Column Layout
    
    # AI Analysis Section
    st.markdown(f"""
        <div style='margin-bottom: 1rem; text-align: center;'>
            <h3 style='color: #1d1d1f; font-size: 1.5rem; font-weight: 600; margin-bottom: 0.5rem;
                       font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;'>
                <i class='fa-solid fa-brain' style='color: #8b5cf6;'></i> {t("ai_analysis")}
            </h3>
            <div style='height: 3px; width: 80px; background: linear-gradient(90deg, #8b5cf6, #06b6d4); margin: 0 auto; border-radius: 2px;'></div>
        </div>
    """, unsafe_allow_html=True)
    
    # Custom HTML Expander with FontAwesome icon
    st.markdown(f"""
    <details style="
        background-color: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 0.5rem 1rem;
        margin-bottom: 1rem;
        transition: all 0.3s ease;">
        <summary style="
            cursor: pointer;
            font-weight: 600;
            color: #475569;
            list-style: none;
            display: flex;
            align-items: center;
            gap: 10px;
            outline: none;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <i class="fa-solid fa-magnifying-glass-chart" style="color: #6366f1;"></i>
                {t('view_detailed_analysis')}
            </div>
            <span style="margin-left: auto; color: #cbd5e1; font-size: 0.8em;">▼</span>
        </summary>
        <div style="
            margin-top: 1rem;
            padding-top: 1rem;
            border-top: 1px solid #f1f5f9;
            color: #1e293b;
            line-height: 1.7;
            animation: fadeIn 0.3s ease-in;">
            {analysis['summary']}
        </div>
    </details>
    <style>
    details > summary::marker {{
        display: none;
    }}
    details[open] summary ~ * {{
        animation: keyframes-fadeIn 0.3s ease-in-out;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    
    report_tools.visualize(df, analysis)


# --- MAIN ROUTER ---
if 'df' not in st.session_state:
    render_selection_screen()
else:
    render_dashboard()
