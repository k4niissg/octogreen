import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
from modules import ai_analysis, report_tools, open_data, ui_utils

# Page Config
st.set_page_config(
    page_title="OctoGreen",
    layout="wide",
    page_icon="assets/logo.png",
    initial_sidebar_state="collapsed"
)

# Apply Clean Apple-Style CSS
st.markdown(ui_utils.CUSTOM_CSS, unsafe_allow_html=True)

# Session State Initialization
if 'data_mode' not in st.session_state:
    st.session_state.data_mode = None  # 'open_data' or 'upload'

def reset_app():
    for key in ['df', 'analysis', 'data_mode']:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

# --- HEADER / HERO SECTION ---
def render_hero():
    # Use standard Streamlit columns to center logo perfectly
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        # Using markdown for centering the image ensures better control than standard st.image centering issues
        try:
            st.image("assets/octogreen-logo.png", width=280)
        except:
             st.markdown("<h1>OctoGreen</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="hero-box">
            <p class="hero-subtitle">Intelligent energy analysis for a sustainable future.<br>Select a data source to begin.</p>
        </div>
    """, unsafe_allow_html=True)

# --- MAIN SELECTION SCREEN ---
def render_selection_screen():
    render_hero()
    
    # Selection Grid
    if st.session_state.data_mode is None:
        # Use columns with explicit padding/gap
        col_space_l, col1, col2, col_space_r = st.columns([1, 2, 2, 1], gap="large")
        
        with col1:
             # Put the button label nicely inside the button or above it
             if st.button("Browse Open Data", key="btn_open_data", width="stretch"):
                st.session_state.data_mode = 'open_data'
                st.rerun()
             st.caption("Public datasets from global repositories")

        with col2:
             if st.button("Upload Your Own", key="btn_upload", width="stretch"):
                st.session_state.data_mode = 'upload'
                st.rerun()
             st.caption("Analyze your CSV files securely")

    # --- Mode: Open Data ---
    elif st.session_state.data_mode == 'open_data':
        c1, c2 = st.columns([1, 5])
        with c1:
            if st.button("Back", key="back_btn"):
                st.session_state.data_mode = None
                st.rerun()
        
        st.markdown("<h3>Select a Dataset</h3>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_opts, col_detais = st.columns([1.2, 0.8], gap="large")
        
        with col_opts:
            source = st.selectbox("Choose Source", [
                "UCI Household (2M+ records)",
                "EPIAS Turkey (Real-time)",
                "World Bank - Energy & Carbon",
            ])
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Action Area
            if "UCI Household" in source:
                if st.button("Download & Analyze Data", key="dl_uci", width="stretch"):
                    with st.status("Processing Data...", expanded=True) as status:
                        st.write("Connecting to safe repository...")
                        time.sleep(0.5)
                        st.write("Downloading 2M+ records...")
                        st.session_state.df = open_data.fetch_kaggle_household()
                        st.write("Running pre-analysis...")
                        time.sleep(0.5)
                        status.update(label="Ready!", state="complete", expanded=False)
                    st.rerun()

            elif "EPIAS Turkey" in source:
                c1, c2 = st.columns(2)
                with c1:
                    start = st.date_input("Start Date", datetime.now() - timedelta(days=7))
                with c2:
                    end = st.date_input("End Date", datetime.now())
                
                if st.button("Fetch Live Data", key="dl_epias", width="stretch"):
                    with st.spinner("Fetching live data..."):
                        df = open_data.fetch_epias_data(start, end)
                        if df is not None:
                            st.session_state.df = df
                            st.rerun()
                        else:
                            st.error("Failed to connect to EPIAS.")
            
            elif "World Bank" in source:
                 if st.button("Fetch World Bank Data", key="dl_wb", width="stretch"):
                    with st.spinner("Accessing World Bank API..."):
                        energy_df = open_data.fetch_world_bank_energy()
                        if energy_df is not None:
                            df = energy_df.copy()
                            df["timestamp"] = pd.to_datetime(df["year"], format="%Y")
                            df["device_id"] = df["country"]
                            df["consumption_kWh"] = df["consumption_kwh_per_capita"]
                            st.session_state.df = df[["timestamp", "device_id", "consumption_kWh"]].dropna()
                            st.rerun()

        with col_detais:
            # Dynamic Info Card based on selection
            if "UCI Household" in source:
                st.markdown("""
                <div class="info-card">
                    <h4>Dataset Snapshot</h4>
                    <div class="metric-value">2M+</div>
                    <p>Individual measurement records</p>
                    <div style="margin-top:1rem; border-top:1px solid #eee; padding-top:1rem;">
                        <p style="font-size:0.9rem; color:#666;"><strong>Contains:</strong><br>Global active power, reactive power, voltage, and intensity measurements.</p>
                        <p style="font-size:0.9rem; color:#666;"><strong>Best for:</strong><br>Deep learning, rigorous statistical analysis.</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif "EPIAS Turkey" in source:
                 st.markdown("""
                <div class="info-card">
                    <h4>Real-Time Feed</h4>
                    <div class="metric-value">Live</div>
                    <p>Energy Exchange Istanbul</p>
                    <div style="margin-top:1rem; border-top:1px solid #eee; padding-top:1rem;">
                        <p style="font-size:0.9rem; color:#666;"><strong>Contains:</strong><br>Hourly electricity consumption data (MWh) across Turkey.</p>
                        <p style="font-size:0.9rem; color:#666;"><strong>Best for:</strong><br>Market analysis, trend forecasting.</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif "World Bank" in source:
                 st.markdown("""
                <div class="info-card">
                    <h4>Global Indicators</h4>
                    <div class="metric-value">190+</div>
                    <p>Countries & Regions</p>
                    <div style="margin-top:1rem; border-top:1px solid #eee; padding-top:1rem;">
                        <p style="font-size:0.9rem; color:#666;"><strong>Contains:</strong><br>Annual energy use metrics per capita.</p>
                        <p style="font-size:0.9rem; color:#666;"><strong>Best for:</strong><br>Macro-economic analysis.</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)


    # --- Mode: Upload ---
    elif st.session_state.data_mode == 'upload':
        c1, c2 = st.columns([1, 5])
        with c1:
            if st.button("← Back", key="back_btn_up"):
                st.session_state.data_mode = None
                st.rerun()
            
        st.markdown("<h3>Upload Your Data</h3>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        uploaded = st.file_uploader("", type=["csv"])
        
        if uploaded:
            st.session_state.df = pd.read_csv(uploaded)
            st.success("File uploaded successfully!")
            time.sleep(1)
            st.rerun()
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(
            "Download CSV Template",
            "timestamp,device_id,consumption_kWh\n2026-01-01 00:00:00,Device_1,0.45\n",
            file_name="template.csv",
        )

# --- DASHBOARD (DATA LOADED) ---
def render_dashboard():
    # Top Bar: Logo Left, New Analysis Right
    c1, c2, c3 = st.columns([1, 4, 1])
    with c1:
        st.image("assets/octogreen-logo.png", width=120)
    with c3:
        if st.button("New Analysis"):
            reset_app()
    
    st.divider()
    
    df = st.session_state.df
    
    # Feature Cards Row using CSS Grid inside Markdown or Columns
    st.markdown("### Dataset Overview")
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Total Records", f"{len(df):,}")
    with m2:
        if 'timestamp' in df.columns:
            st.metric("Timeline", "Time Series Data")
        else:
            st.metric("Structure", "Tabular")
    with m3:
        if 'device_id' in df.columns:
            st.metric("Sources", f"{df['device_id'].nunique()}")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Main Content Area
    col_main, col_side = st.columns([2, 1], gap="large")
    
    with col_main:
        # AI Analysis Section
        st.subheader("AI Analysis")
        
        analysis = st.session_state.get('analysis')
        if analysis is None:
            with st.spinner("Processing advanced analytics..."):
                analysis = ai_analysis.analyze(df)
            st.session_state.analysis = analysis
            
        # Display AI summary in a collapsible expander
        with st.expander("VIEW DETAILED AI ANALYSIS", expanded=False):
            st.markdown(f"""
            <div style="background:white; padding:1.5rem; border-radius:12px; border:1px solid #e5e5e5; margin-bottom:1rem;">
                <p style="color:#1D1D1F; font-size:1.05rem; line-height:1.6;">{analysis['summary']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Visualization Header with custom styling to match other headers
        st.markdown("<h3 style='color:#1D1D1F; border-bottom: 1px solid #e5e7eb; padding-bottom: 0.5rem; margin-top:2rem;'>Visualization</h3>", unsafe_allow_html=True)
        report_tools.visualize(df, analysis)

    with col_side:
        st.subheader("Key Findings")
        st.info(analysis['recommendations'])
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Export")
        report_tools.download_buttons(df, analysis)


# --- MAIN ROUTER ---
if 'df' not in st.session_state:
    render_selection_screen()
else:
    render_dashboard()