"""Icon and styling utilities for OctoGreen - Apple Inspired Design"""

# Clean, Robust Apple-Style CSS
CUSTOM_CSS = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Base Settings */
:root {
    --bg-color: #ffffff;
    --bg-gradient: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    --text-primary: #1d1d1f;
    --text-secondary: #86868b;
    --accent: #0071e3;
    --accent-gradient: linear-gradient(135deg, #0071e3 0%, #0056b3 100%);
    --card-border: #d2d2d7;
    --success-gradient: linear-gradient(135deg, #10b981 0%, #059669 100%);
}

.stApp {
    background: var(--bg-gradient) !important;
    font-family: 'Inter', sans-serif !important;
}

/* Hide Streamlit Default Elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stSidebar"] {display: none;}

/* Typography */
h1, h2, h3 {
    text-align: center !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--text-primary) !important;
}

p {
    font-size: 1.05rem !important;
    line-height: 1.5 !important;
    color: var(--text-secondary) !important;
}

/* Center everything in main container & widen it */
.block-container {
    max-width: 1200px !important;
    padding-top: 2rem !important;
    padding-bottom: 5rem !important;
}

/* Hero Section - Premium Design */
.hero-box {
    text-align: center;
    padding: 3rem 2rem;
    margin-bottom: 3rem;
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(10px);
    border-radius: 24px;
    border: 1px solid rgba(255, 255, 255, 0.8);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.06);
}

.hero-subtitle {
    font-size: 1.3rem !important;
    color: var(--text-secondary) !important;
    margin-top: 1rem !important;
    font-weight: 400;
    line-height: 1.6 !important;
}

/* Selection Cards (Containers for Buttons) - Premium Design */
div.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
    color: var(--text-primary) !important;
    border: 2px solid rgba(0, 113, 227, 0.1) !important;
    border-radius: 16px !important;
    padding: 2rem 1.5rem !important;
    font-size: 1.2rem !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08), 0 0 0 1px rgba(0, 0, 0, 0.02) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
}

div.stButton > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--accent-gradient);
    opacity: 0;
    transition: opacity 0.3s ease;
    border-radius: 16px;
}

div.stButton > button:hover {
    border-color: var(--accent) !important;
    box-shadow: 0 8px 30px rgba(0, 113, 227, 0.25), 0 0 0 1px rgba(0, 113, 227, 0.1) !important;
    transform: translateY(-4px) scale(1.02) !important;
}

div.stButton > button:hover::before {
    opacity: 0.05;
}

div.stButton > button:active {
    transform: translateY(-2px) scale(1.01) !important;
    box-shadow: 0 4px 15px rgba(0, 113, 227, 0.2) !important;
}

/* Force light theme on Inputs (Selectbox, DateInput, etc.) */
div[data-baseweb="select"] > div, 
div[data-baseweb="input"] > div,
div[data-baseweb="base-input"] {
    background-color: white !important;
    color: #1d1d1f !important;
    border-color: #d2d2d7 !important;
}

/* Force text color inside inputs */
input, .stSelectbox div {
   color: #1d1d1f !important;
}

/* Force light theme on Status/Spinner */
div[data-testid="stStatusWidget"] {
    background-color: white !important;
    color: #1d1d1f !important;
    border: 1px solid #d2d2d7 !important;
}

/* Inputs wrapper */
.stSelectbox > div > div, .stTextInput > div > div, .stDateInput > div > div {
    border-radius: 8px !important;
    border-color: #d2d2d7 !important;
    background-color: white !important;
    color: #1d1d1f !important;
}

/* Expander styling - Premium AI Analysis Button */
.streamlit-expanderHeader {
    background: var(--accent-gradient) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-size: 1.05rem !important;
    padding: 1.2rem 1.5rem !important;
    box-shadow: 0 4px 20px rgba(0, 113, 227, 0.3), 0 0 0 1px rgba(0, 113, 227, 0.1) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    letter-spacing: 0.5px !important;
}

.streamlit-expanderHeader:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 30px rgba(0, 113, 227, 0.4), 0 0 0 1px rgba(0, 113, 227, 0.2) !important;
}

.streamlit-expanderHeader svg {
    fill: white !important;
}

/* Expander content area */
details[open] > .streamlit-expanderHeader {
    border-radius: 12px 12px 0 0 !important;
}

details > div {
    border: 2px solid rgba(0, 113, 227, 0.1) !important;
    border-top: none !important;
    border-radius: 0 0 12px 12px !important;
    background: white !important;
}

/* Force Light Theme for DataFrames & Tables */
[data-testid="stDataFrame"] {
    background-color: white !important;
    color: #1d1d1f !important;
    border: 1px solid #e5e5e5;
    border-radius: 8px;
}
[data-testid="stDataFrame"] div[role="grid"] {
    color: #1d1d1f !important;
}
[data-testid="stDataFrame"] div[role="columnheader"] {
    background-color: #f5f5f7 !important;
    color: #1d1d1f !important;
    font-weight: 600 !important;
}

/* Force White Buttons (Secondary) */
button:not(.primary-action-btn button) {
    background-color: white !important;
    color: #1d1d1f !important;
    border: 1px solid #d2d2d7 !important;
}
button:not(.primary-action-btn button):hover {
    border-color: #0071e3 !important;
    color: #0071e3 !important;
    background-color: white !important;
}

/* Info Card Style - Premium Glassmorphism */
.info-card {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.9);
    border-radius: 16px;
    padding: 2rem;
    text-align: left;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease;
}

.info-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
}

.info-card h4 {
    text-align: left !important;
    margin-top: 0 !important;
    color: var(--accent) !important;
    font-size: 1.1rem !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 700 !important;
}

.metric-value {
    font-size: 3rem;
    font-weight: 800;
    background: var(--accent-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0.5rem 0;
}

/* Fix Plotly Modebar styling (remove grey backgrounds, fix icons) */
.js-plotly-plot .plotly .modebar {
    background-color: transparent !important;
    border: none !important;
}
.js-plotly-plot .plotly .modebar-group {
    background-color: transparent !important;
}
.js-plotly-plot .plotly .modebar-btn {
    background-color: transparent !important;
}
.js-plotly-plot .plotly .modebar-btn path {
    fill: #86868b !important;
}
.js-plotly-plot .plotly .modebar-btn.active path,
.js-plotly-plot .plotly .modebar-btn:hover path {
    fill: #0071e3 !important;
}

/* --- ANIMATIONS (Apple-like smooth entry) --- */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeScale {
    from {
        opacity: 0;
        transform: scale(0.98);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

/* Apply animations */
.hero-box {
    animation: fadeInUp 0.8s ease-out forwards;
}

/* Staggered animation for inputs/buttons container if possible, 
   but globally applying to buttons gives a nice effect on load */
div.stButton > button {
    animation: fadeScale 0.6s ease-out forwards;
    animation-delay: 0.2s; /* Slight delay after hero */
    opacity: 0; /* Star invisible */
}

/* Info cards and metrics */
.info-card, .metric-card {
    animation: fadeInUp 0.7s ease-out forwards;
    opacity: 0;
    animation-delay: 0.3s;
}

/* Center Logo Image Container */
div[data-testid="stImage"] {
    display: flex;
    justify-content: center;
    align-items: center;
    animation: fadeScale 0.8s ease-out;
}
</style>
'''

def show_loading_progress(message, steps=None):
    """Show minimal loading progress"""
    import streamlit as st
    import time
    
    if steps:
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, step in enumerate(steps):
            status_text.markdown(f"<p style='text-align:center; color:#86868B; font-size:0.9rem; margin-bottom:0.5rem;'>{step}</p>", unsafe_allow_html=True)
            progress_bar.progress((i + 1) / len(steps))
            time.sleep(0.15)
        
        status_text.markdown(f"<p style='text-align:center; color:#34C759; font-weight:500; margin-bottom:0.5rem;'>✓ {message}</p>", unsafe_allow_html=True)
        time.sleep(0.5)
        progress_bar.empty()
        status_text.empty()
    else:
        with st.spinner(f"{message}"):
            time.sleep(0.3)