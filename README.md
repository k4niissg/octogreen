# OctoGreen: Smart Energy Analysis and Savings Platform

## Project Purpose
A platform that analyzes energy consumption data from IoT devices and manual uploads, providing anomaly detection, personalized savings recommendations, and carbon footprint calculations, supported by a modern visual dashboard.

## Key Features
- IoT data simulator and manual CSV upload
- AI-based analysis: consumption patterns, anomaly detection, scenario generation
- Personalized recommendation engine (% savings, USD and carbon equivalent)
- Live and visual dashboard (Streamlit)
- PDF/CSV report download
- Real IoT device integration (Tuya, Shelly, MQTT)
- Open data sources integration (UCI, EPIAS, etc.)
- Bill-based estimation
- Device-based estimation

## Usage
1. Start the application with Streamlit:
   ```bash
   streamlit run app.py
   ```
2. Load or simulate data through the dashboard.
3. View analyses and recommendations, download reports.

## Requirements
- Python 3.9+
- Required packages: pandas, numpy, scikit-learn, streamlit, plotly, fpdf, requests, paho-mqtt

## Installation
```bash
pip install -r requirements.txt
```

## Data Sources
- **IoT Simulation**: Generate synthetic data for testing
- **CSV Upload**: Upload your own consumption data
- **Real IoT Devices**: Connect Tuya, Shelly, or MQTT devices
- **Bill Estimation**: Estimate hourly consumption from monthly bills
- **Device Estimation**: Calculate consumption based on device specifications
- **Open Data**: Access UCI Household, EPIAS Turkey, and sample datasets

## CSV Format
```csv
timestamp,device_id,consumption_kWh
2024-01-15 00:00:00,Refrigerator,0.45
2024-01-15 01:00:00,Refrigerator,0.51
2024-01-15 00:00:00,AC,1.20
```

## Features
- **Anomaly Detection**: Machine learning-based anomaly identification
- **Pattern Analysis**: Hourly and daily consumption patterns
- **Savings Recommendations**: Personalized tips with kWh, CO2, and USD savings
- **Carbon Footprint**: Calculate environmental impact
- **Interactive Charts**: Plotly-powered visualizations
- **Export Reports**: PDF and CSV formats

## Contributing and License
Solo hackathon project. For demo and presentation purposes.
