import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from modules import data_simulator, ai_analysis, report_tools, manual_data, open_data
try:
    from modules import iot_connector
    IOT_AVAILABLE = True
except ImportError:
    IOT_AVAILABLE = False

st.set_page_config(page_title="OctoGreen Dashboard", layout="wide")

st.title("🌱 OctoGreen: Smart Energy Analysis Platform")

# Sidebar: Data Source Selection
st.sidebar.header("Data Source")
options = ["IoT Simulation", "Upload CSV", "Bill Estimation", "Device Estimation", "Open Data Sources"]
if IOT_AVAILABLE:
    options.insert(1, "Real IoT Devices")
data_source = st.sidebar.radio("How to load data?", options)

if data_source == "IoT Simulation":
    num_devices, days = data_simulator.get_simulation_options()
    df = data_simulator.generate_iot_data(num_devices=num_devices, days=days)
    st.success(f"Simulated IoT data loaded for {num_devices} devices and {days} days.")
    data_simulator.download_simulated_csv(df)

elif data_source == "Real IoT Devices":
    st.sidebar.subheader("IoT Settings")
    iot_type = st.sidebar.selectbox("Device Type", ["Tuya Smart", "Shelly", "MQTT"])
    if iot_type == "Tuya Smart":
        api_key = st.sidebar.text_input("API Key", type="password")
        device_ids = st.sidebar.text_area("Device IDs (one per line)").split("\n")
        if st.sidebar.button("Fetch Data"):
            df = iot_connector.fetch_from_tuya(api_key, device_ids, None, None)
            st.success("Data fetched from Tuya devices.")
    st.info("Enter your API credentials for IoT integration.")
    st.stop()

elif data_source == "Bill Estimation":
    st.sidebar.subheader("Bill Information")
    total_kwh = st.sidebar.number_input("Monthly Total Consumption (kWh)", min_value=0.0, value=300.0)
    month = st.sidebar.selectbox("Month", range(1, 13), index=0)
    year = st.sidebar.number_input("Year", min_value=2020, max_value=2030, value=2024)
    df = manual_data.create_from_monthly_bill(total_kwh, month, year)
    st.success(f"Hourly estimation created from {total_kwh} kWh monthly consumption.")

elif data_source == "Device Estimation":
    st.sidebar.subheader("Add Your Devices")
    num_devices = st.sidebar.number_input("How many devices?", min_value=1, max_value=20, value=3)
    devices = {}
    for i in range(num_devices):
        with st.sidebar.expander(f"Device {i+1}"):
            name = st.text_input(f"Device Name", value=f"Device_{i+1}", key=f"name_{i}")
            watt = st.number_input(f"Power (Watt)", min_value=1, value=100, key=f"watt_{i}")
            hours = st.number_input(f"Daily Usage (Hours)", min_value=1, max_value=24, value=8, key=f"hours_{i}")
            devices[name] = {"watt": watt, "hours_per_day": hours}
    df = manual_data.create_from_device_estimates(devices)
    st.success(f"Estimation created for {num_devices} devices.")

elif data_source == "Open Data Sources":
    st.sidebar.subheader("Select Data Source")
    source = st.sidebar.selectbox("Source", [
        "UCI Household (2M+ records)",
        "EPIAS Turkey (Real-time)",
        "World Bank - Energy & Carbon",
        "OECD Energy Statistics",
        "EU Open Data Portal",
        "London Smart Meter Data",
        "Sample Datasets"
    ])
    
    if source == "UCI Household (2M+ records)":
        if st.sidebar.button("Download Data"):
            with st.spinner("Downloading UCI dataset..."):
                df = open_data.fetch_kaggle_household()
                st.success(f"{len(df)} records loaded!")
        else:
            st.info("👆 Click 'Download Data' button")
            st.stop()
    
    elif source == "EPIAS Turkey (Real-time)":
        start = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=7))
        end = st.sidebar.date_input("End Date", datetime.now())
        if st.sidebar.button("Fetch Data"):
            with st.spinner("Fetching data from EPIAS..."):
                df = open_data.fetch_epias_data(start, end)
                if df is not None:
                    st.success("Turkey electricity consumption data loaded!")
                else:
                    st.error("Failed to fetch data. Check API access.")
                    st.stop()
        else:
            st.info("👆 Select dates and click 'Fetch Data' button")
            st.stop()
    
    elif source == "World Bank - Energy & Carbon":
        if st.sidebar.button("Fetch World Bank Data"):
            with st.spinner("Fetching World Bank data..."):
                energy_df = open_data.fetch_world_bank_energy()
                carbon_df = open_data.fetch_world_bank_carbon()
                if energy_df is not None:
                    st.success(f"World Bank data loaded! {len(energy_df)} records")
                    st.dataframe(energy_df.head())
                    df = energy_df.copy()
                    df["timestamp"] = pd.to_datetime(df["year"], format="%Y")
                    df["device_id"] = df["country"]
                    df["consumption_kWh"] = df["consumption_kwh_per_capita"]
                    df = df[["timestamp", "device_id", "consumption_kWh"]].dropna()
                else:
                    st.error("Failed to fetch World Bank data.")
                    st.stop()
        else:
            st.info("👆 Click 'Fetch World Bank Data' button")
            st.stop()
    
    elif source == "OECD Energy Statistics":
        if st.sidebar.button("Fetch OECD Data"):
            with st.spinner("Fetching OECD data..."):
                oecd_data = open_data.fetch_oecd_energy()
                if oecd_data:
                    st.success("OECD energy statistics loaded!")
                    st.json(oecd_data)
                    st.info("Data structure: OECD energy statistics for OECD countries (2015-2023)")
                    df = pd.DataFrame({"timestamp": [datetime.now()], "device_id": ["OECD"], "consumption_kWh": [0]})
                else:
                    st.error("Failed to fetch OECD data.")
                    st.stop()
        else:
            st.info("👆 Click 'Fetch OECD Data' button")
            st.stop()
    
    elif source == "EU Open Data Portal":
        if st.sidebar.button("Fetch EU Data"):
            with st.spinner("Fetching EU Open Data..."):
                eu_data = open_data.fetch_eu_open_data()
                if eu_data:
                    st.success("EU Open Data loaded!")
                    st.json(eu_data)
                    st.info("Available datasets from EU Open Data Portal")
                    df = pd.DataFrame({"timestamp": [datetime.now()], "device_id": ["EU"], "consumption_kWh": [0]})
                else:
                    st.error("Failed to fetch EU data.")
                    st.stop()
        else:
            st.info("👆 Click 'Fetch EU Data' button")
            st.stop()
    
    elif source == "London Smart Meter Data":
        if st.sidebar.button("Fetch London Data"):
            with st.spinner("Fetching London smart meter data..."):
                london_data = open_data.fetch_london_smart_meter()
                if london_data:
                    st.success("London smart meter datasets found!")
                    st.json(london_data)
                    st.info("Smart meter energy use data from London Data Store")
                    df = pd.DataFrame({"timestamp": [datetime.now()], "device_id": ["London"], "consumption_kWh": [0]})
                else:
                    st.error("Failed to fetch London data.")
                    st.stop()
        else:
            st.info("👆 Click 'Fetch London Data' button")
            st.stop()
    
    else:  # Sample Datasets
        if st.sidebar.button("Download Sample Data"):
            with st.spinner("Downloading sample datasets..."):
                datasets = open_data.download_sample_datasets()
                if datasets:
                    df = pd.concat(datasets.values(), ignore_index=True)
                    st.success(f"{len(datasets)} datasets merged!")
                else:
                    st.error("Failed to download data.")
                    st.stop()
        else:
            st.info("👆 Click 'Download Sample Data' button")
            st.stop()

else:
    uploaded = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
    st.sidebar.download_button(
        "Download sample CSV template",
        "timestamp,device_id,consumption_kWh\n2026-01-01 00:00:00,Device_1,0.45\n2026-01-01 01:00:00,Device_1,0.51\n2026-01-01 00:00:00,Device_2,0.38\n",
        file_name="sample_template.csv"
    )
    if uploaded:
        df = pd.read_csv(uploaded)
        st.success("CSV data loaded.")
    else:
        st.warning("Please upload a CSV file.")
        st.stop()

# Data Preview
st.subheader("Data Preview")
st.dataframe(df.head())

# AI Analysis and Recommendations
analysis = ai_analysis.analyze(df)
st.subheader("AI Analysis Results and Recommendations")
st.write(analysis["summary"])
st.write(analysis["recommendations"])

# Reporting
st.subheader("Download Report")
report_tools.download_buttons(df, analysis)

# Visualization
st.subheader("Consumption Charts and Carbon Footprint")
report_tools.visualize(df, analysis)
