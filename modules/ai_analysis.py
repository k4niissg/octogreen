import pandas as pd
import numpy as np

def analyze(df):
    from sklearn.ensemble import IsolationForest
    summary = {}
    recommendations = []
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    # Daily total, average, peak hours
    daily = df.groupby(df['timestamp'].dt.date)['consumption_kWh'].sum()
    hourly = df.groupby(df['timestamp'].dt.hour)['consumption_kWh'].mean()
    summary['daily_total'] = daily.to_dict()
    summary['hourly_avg'] = hourly.to_dict()
    # Anomaly detection: IsolationForest
    model = IsolationForest(contamination=0.03, random_state=42)
    df['anomaly'] = model.fit_predict(df[['consumption_kWh']])
    anomalies = df[df['anomaly'] == -1]
    summary['anomalies'] = anomalies.to_dict('records')
    # Device-based analysis and recommendations
    device_totals = df.groupby('device_id')['consumption_kWh'].sum()
    device_hourly = df.groupby(['device_id', df['timestamp'].dt.hour])['consumption_kWh'].mean().unstack()
    top_device = device_totals.idxmax()
    peak_hour = device_hourly.loc[top_device].idxmax()
    savings_kwh = device_totals.max() * 0.15
    carbon_factor = 0.4
    savings_carbon = savings_kwh * carbon_factor
    kwh_price = 1.5  # USD/kWh example
    savings_usd = savings_kwh * kwh_price
    recommendations.append(
        f"For 15% savings, turn off {top_device} device around {peak_hour}:00. Estimated savings: {savings_kwh:.2f} kWh, {savings_carbon:.2f} kg CO2, ${savings_usd:.2f}"
    )
    # Scenario: If all devices shut down 1 hour earlier
    scenario_saving = df[df['timestamp'].dt.hour == 23]['consumption_kWh'].sum()
    scenario_carbon = scenario_saving * carbon_factor
    scenario_usd = scenario_saving * kwh_price
    recommendations.append(
        f"If all devices shut down 1 hour earlier: {scenario_saving:.2f} kWh, {scenario_carbon:.2f} kg CO2, ${scenario_usd:.2f} savings."
    )
    # Summary
    summary['top_device'] = top_device
    summary['peak_hour'] = int(peak_hour)
    summary['tasarruf_kwh'] = float(savings_kwh)
    summary['tasarruf_carbon'] = float(savings_carbon)
    summary['tasarruf_tl'] = float(savings_usd)
    return {'summary': summary, 'recommendations': recommendations}
