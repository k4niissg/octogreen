import pandas as pd
import requests
from datetime import datetime

def fetch_from_tuya(api_key, device_ids, start_date, end_date):
    """Fetch data from Tuya Smart plugs"""
    data = []
    # Tuya API integration
    headers = {"Authorization": f"Bearer {api_key}"}
    for device_id in device_ids:
        response = requests.get(
            f"https://openapi.tuyaus.com/v1.0/devices/{device_id}/logs",
            headers=headers,
            params={"start_time": start_date, "end_time": end_date}
        )
        if response.ok:
            logs = response.json()["result"]
            for log in logs:
                data.append({
                    "timestamp": datetime.fromtimestamp(log["time"]),
                    "device_id": device_id,
                    "consumption_kWh": log["value"] / 1000
                })
    return pd.DataFrame(data)

def fetch_from_shelly(device_ips):
    """Fetch data from Shelly smart plugs"""
    data = []
    for ip in device_ips:
        response = requests.get(f"http://{ip}/status")
        if response.ok:
            status = response.json()
            data.append({
                "timestamp": datetime.now(),
                "device_id": ip,
                "consumption_kWh": status["meters"][0]["power"] / 1000
            })
    return pd.DataFrame(data)

def fetch_from_mqtt(broker, topic, username, password):
    """Fetch data from MQTT broker (Zigbee, Home Assistant, etc.)"""
    import paho.mqtt.client as mqtt
    data = []
    
    def on_message(client, userdata, msg):
        import json
        payload = json.loads(msg.payload)
        data.append({
            "timestamp": datetime.now(),
            "device_id": msg.topic.split("/")[-1],
            "consumption_kWh": payload.get("power", 0) / 1000
        })
    
    client = mqtt.Client()
    client.username_pw_set(username, password)
    client.on_message = on_message
    client.connect(broker, 1883, 60)
    client.subscribe(topic)
    client.loop_start()
    return data
