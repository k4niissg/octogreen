import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
from modules import ai_analysis, report_tools, open_data, ui_utils

st.set_page_config(
    page_title="OctoGreen Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="assets/logo.png"
)

st.markdown(ui_utils.CUSTOM_CSS, unsafe_allow_html=True)

# Sidebar content (always visible)
try:
    st.sidebar.image("assets/octogreen-logo.png", width='stretch')
except:
    st.sidebar.markdown('<div style="width:100%;height:200px;background:#10b981;border-radius:20px;margin-bottom:1rem;"></div>', unsafe_allow_html=True)

# Show Load New Data button if data is loaded
if 'df' in st.session_state:
    st.sidebar.markdown("---")
    st.sidebar.markdown("<h3 style='color:#10b981;margin-bottom:2rem;'>Current Data</h3>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<p style='color:#374151;'>Dataset loaded with {len(st.session_state.df)} records</p>", unsafe_allow_html=True)
    if st.sidebar.button("Load New Data"):
        if 'analysis' in st.session_state:
            del st.session_state.analysis
        del st.session_state.df
        st.rerun()
    st.sidebar.markdown("---")

# Check if data is loaded
if 'df' not in st.session_state:
    # Show welcome screen
    ui_utils.show_welcome_screen()
    
    # Sidebar for data source selection
    st.sidebar.markdown("<h3 style='color:#10b981;margin-bottom:2rem;'>Data Source</h3>", unsafe_allow_html=True)
    data_source = st.sidebar.radio("How to load data?", ["Open Data Sources", "Upload CSV"], index=0)
    
    if data_source == "Open Data Sources":
        st.sidebar.markdown("<h4 style='margin-bottom:1rem;'>Select Data Source</h4>", unsafe_allow_html=True)
        source = st.sidebar.selectbox("Source", [
            "UCI Household (2M+ records)",
            "EPIAS Turkey (Real-time)",
            "World Bank - Energy & Carbon",
            "OECD Energy Statistics",
            "EU Open Data Portal",
            "London Smart Meter Data",
            "Sample Datasets"
        ])
        
        if "UCI Household" in source:
            if st.sidebar.button("Download Data", key="uci_btn"):
                # Create progress bar and status in main content area
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Initial state
                status_text.info(" Preparing to download data...")
                progress_bar.progress(10)
                
                try:
                    # Show loading during data fetching
                    with st.spinner("Downloading data from UCI repository..."):
                        progress_bar.progress(30)
                        st.session_state.df = open_data.fetch_kaggle_household()
                        progress_bar.progress(80)
                    
                    # Clear previous analysis
                    if 'analysis' in st.session_state:
                        del st.session_state.analysis
                    
                    # Show success
                    progress_bar.progress(100)
                    status_text.success(f" Successfully loaded {len(st.session_state.df)} records!")
                    
                    # Keep the success message visible briefly before rerun
                    time.sleep(1.5)
                    st.rerun()
                    
                except Exception as e:
                    progress_bar.empty()
                    status_text.error(f" Error loading data: {str(e)}")
            # No message will be shown when the button is not clicked
        
        elif "EPIAS Turkey" in source:
            start = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=7))
            end = st.sidebar.date_input("End Date", datetime.now())
            if st.sidebar.button("Fetch Data", key="epias_fetch"):
                # Create progress bar and status in main content area
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                try:
                    # Initial state
                    status_text.info(" Connecting to EPIAS API...")
                    progress_bar.progress(10)
                    
                    # Show loading during data fetching
                    with st.spinner("Fetching electricity consumption data..."):
                        progress_bar.progress(30)
                        df = open_data.fetch_epias_data(start, end)
                        
                        if df is not None:
                            progress_bar.progress(70)
                            st.session_state.df = df
                            
                            # Clear previous analysis
                            if 'analysis' in st.session_state:
                                del st.session_state.analysis
                            
                            # Show success
                            progress_bar.progress(100)
                            status_text.success(" Successfully loaded Turkey electricity consumption data!")
                            
                            # Keep the success message visible briefly before rerun
                            time.sleep(1.5)
                            st.rerun()
                        else:
                            progress_bar.empty()
                            status_text.error(" Failed to fetch data. Please check your API access and try again.")
                            
                except Exception as e:
                    progress_bar.empty()
                    status_text.error(f" Error: {str(e)}")
            else:
                st.info("↑ Select date range and click 'Fetch Data' button")
        
        elif "World Bank" in source:
            if st.sidebar.button("Fetch World Bank Data"):
                # Show loading during actual data fetching
                with st.sidebar.spinner("Connecting to World Bank API..."):
                    energy_df = open_data.fetch_world_bank_energy()
                if energy_df is not None:
                    st.success(f"✓ World Bank data loaded! {len(energy_df)} records")
                    df = energy_df.copy()
                    df["timestamp"] = pd.to_datetime(df["year"], format="%Y")
                    df["device_id"] = df["country"]
                    df["consumption_kWh"] = df["consumption_kwh_per_capita"]
                    st.session_state.df = df[["timestamp", "device_id", "consumption_kWh"]].dropna()
                    if 'analysis' in st.session_state:
                        del st.session_state.analysis
                    st.rerun()
                else:
                    st.error("✗ Failed to fetch World Bank data.")
            else:
                st.info("↑ Click 'Fetch World Bank Data' button")
        
        else:
            st.info("Select a data source and click the corresponding button")
    
    else:  # Upload CSV
        uploaded = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
        st.sidebar.download_button(
            "Download sample CSV template",
            "timestamp,device_id,consumption_kWh\n2026-01-01 00:00:00,Device_1,0.45\n2026-01-01 01:00:00,Device_1,0.51\n2026-01-01 00:00:00,Device_2,0.38\n",
            file_name="sample_template.csv"
        )
        if uploaded:
            st.session_state.df = pd.read_csv(uploaded)
            if 'analysis' in st.session_state:
                del st.session_state.analysis
            st.success("✓ CSV data loaded.")
            st.rerun()
        else:
            st.markdown(
                """
                <div style='background-color:#fffbe6; color:#b8860b; padding:12px 18px; border-radius:6px; font-size:1.1rem; font-weight:bold; border:1px solid #ffe58f;'>
                ⚠ Please upload a CSV file.
                </div>
                """,
                unsafe_allow_html=True
            )

else:
    # Data is loaded, show analysis
    df = st.session_state.df
    
    # Simple header for analysis page
    st.markdown("<h1 style='text-align:center;'>OctoGreen: Smart Energy Analysis Platform</h1>", unsafe_allow_html=True)
    
    # Data Preview
    st.markdown("<h2>Data Preview</h2>", unsafe_allow_html=True)
    st.dataframe(df.head())
    
    # AI Analysis
    analysis = st.session_state.get('analysis')
    if analysis is None:
        with st.spinner("Running AI analysis..."):
            analysis = ai_analysis.analyze(df)
        st.session_state.analysis = analysis
    st.markdown("<h2>AI Analysis Results and Recommendations</h2>", unsafe_allow_html=True)
    st.write(analysis["summary"])
    st.write(analysis["recommendations"])
    
    # Reporting
    st.markdown("<h2>Download Report</h2>", unsafe_allow_html=True)
    report_tools.download_buttons(df, analysis)
    
    # Visualization
    st.markdown("<h2>Consumption Charts and Carbon Footprint</h2>", unsafe_allow_html=True)
    report_tools.visualize(df, analysis)