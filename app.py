import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from modules import ai_analysis, report_tools, open_data, ui_utils

st.set_page_config(
    page_title="OctoGreen Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="assets/logo.png"
)

st.markdown(ui_utils.CUSTOM_CSS, unsafe_allow_html=True)

# Check if data is loaded
if 'df' not in st.session_state:
    # Show welcome screen
    ui_utils.show_welcome_screen()
    
    # Sidebar logo at top (centered and larger)
    try:
        st.sidebar.image("assets/octogreen-logo.png", use_container_width=True)
    except:
        st.sidebar.markdown('<div style="width:100%;height:200px;background:#10b981;border-radius:20px;margin-bottom:1rem;"></div>', unsafe_allow_html=True)
    
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
                ui_utils.show_loading_progress("UCI dataset loaded!", [
                    "Connecting to UCI repository...",
                    "Downloading household data...",
                    "Processing 2M+ records...",
                    "Cleaning and formatting data..."
                ])
                st.session_state.df = open_data.fetch_kaggle_household()
                st.success(f"✓ {len(st.session_state.df)} records loaded!")
                st.rerun()
            else:
                st.info("Click 'Download Data' button")
        
        elif "EPIAS Turkey" in source:
            start = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=7))
            end = st.sidebar.date_input("End Date", datetime.now())
            if st.sidebar.button("Fetch Data"):
                ui_utils.show_loading_progress("Turkey data loaded!", [
                    "Connecting to EPIAS API...",
                    "Fetching electricity consumption data...",
                    "Processing hourly records..."
                ])
                df = open_data.fetch_epias_data(start, end)
                if df is not None:
                    st.session_state.df = df
                    st.success("✓ Turkey electricity consumption data loaded!")
                    st.rerun()
                else:
                    st.error("✗ Failed to fetch data. Check API access.")
            else:
                st.info("↑ Select dates and click 'Fetch Data' button")
        
        elif "World Bank" in source:
            if st.sidebar.button("Fetch World Bank Data"):
                ui_utils.show_loading_progress("World Bank data loaded!", [
                    "Connecting to World Bank API...",
                    "Fetching energy consumption indicators...",
                    "Processing country-level data...",
                    "Formatting for analysis..."
                ])
                energy_df = open_data.fetch_world_bank_energy()
                if energy_df is not None:
                    st.success(f"✓ World Bank data loaded! {len(energy_df)} records")
                    df = energy_df.copy()
                    df["timestamp"] = pd.to_datetime(df["year"], format="%Y")
                    df["device_id"] = df["country"]
                    df["consumption_kWh"] = df["consumption_kwh_per_capita"]
                    st.session_state.df = df[["timestamp", "device_id", "consumption_kWh"]].dropna()
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
    
    # Clear data button
    if st.sidebar.button("Load New Data"):
        del st.session_state.df
        st.rerun()
    
    # Data Preview
    st.markdown("<h2>Data Preview</h2>", unsafe_allow_html=True)
    st.dataframe(df.head())
    
    # AI Analysis
    analysis = ai_analysis.analyze(df)
    st.markdown("<h2>AI Analysis Results and Recommendations</h2>", unsafe_allow_html=True)
    st.write(analysis["summary"])
    st.write(analysis["recommendations"])
    
    # Reporting
    st.markdown("<h2>Download Report</h2>", unsafe_allow_html=True)
    report_tools.download_buttons(df, analysis)
    
    # Visualization
    st.markdown("<h2>Consumption Charts and Carbon Footprint</h2>", unsafe_allow_html=True)
    report_tools.visualize(df, analysis)