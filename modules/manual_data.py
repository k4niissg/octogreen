import pandas as pd
from datetime import datetime, timedelta

def create_from_monthly_bill(total_kwh, month, year, num_devices=1):
    """Hourly estimation from monthly bill total"""
    days_in_month = 30
    hours = days_in_month * 24
    avg_hourly = total_kwh / hours
    
    start_date = datetime(year, month, 1)
    timestamps = pd.date_range(start_date, periods=hours, freq='H')
    
    data = []
    for ts in timestamps:
        # Night hours lower, daytime higher consumption
        hour = ts.hour
        if 0 <= hour < 6:
            multiplier = 0.6
        elif 6 <= hour < 9 or 18 <= hour < 23:
            multiplier = 1.4
        else:
            multiplier = 1.0
            
        data.append({
            "timestamp": ts,
            "device_id": "Home_Total",
            "consumption_kWh": round(avg_hourly * multiplier, 3)
        })
    
    return pd.DataFrame(data)

def create_from_device_estimates(devices_dict):
    """Create data from device-based estimates
    
    Example:
    devices = {
        "Refrigerator": {"watt": 150, "hours_per_day": 24},
        "AC": {"watt": 2000, "hours_per_day": 8},
        "TV": {"watt": 100, "hours_per_day": 6}
    }
    """
    data = []
    start = datetime.now() - timedelta(days=7)
    
    for device, specs in devices_dict.items():
        daily_kwh = (specs["watt"] * specs["hours_per_day"]) / 1000
        hourly_kwh = daily_kwh / specs["hours_per_day"]
        
        for day in range(7):
            for hour in range(24):
                if hour < specs["hours_per_day"]:
                    ts = start + timedelta(days=day, hours=hour)
                    data.append({
                        "timestamp": ts,
                        "device_id": device,
                        "consumption_kWh": round(hourly_kwh, 3)
                    })
    
    return pd.DataFrame(data)
