import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_iot_data(num_devices=5, days=7):
    np.random.seed(42)
    timestamps = pd.date_range(datetime.now() - timedelta(days=days), periods=days*24, freq='H')
    data = []
    for device in range(1, num_devices+1):
        consumption = np.abs(np.random.normal(loc=0.5, scale=0.2, size=len(timestamps)))
        for t, c in zip(timestamps, consumption):
            data.append({
                'timestamp': t,
                'device_id': f'Cihaz_{device}',
                'consumption_kWh': round(c, 3)
            })
    df = pd.DataFrame(data)
    return df

def get_simulation_options():
    """Streamlit interface for device and day count selection"""
    import streamlit as st
    num_devices = st.sidebar.slider("Number of Devices", 1, 10, 5)
    days = st.sidebar.slider("How many days of data?", 1, 30, 7)
    return num_devices, days

def download_simulated_csv(df):
    import streamlit as st
    st.download_button("Download simulated data as CSV", df.to_csv(index=False), file_name="simulated_data.csv")
