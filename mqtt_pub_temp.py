import paho.mqtt.client as mqtt
import time
import random
import json
from datetime import datetime

# MQTT Broker Configuration
BROKER = "localhost"  # Change to your broker IP if remote
PORT = 1883
TOPIC = "sensors/temperature"
CLIENT_ID = "temperature_publisher"

# Student ID
STUDENT_ID = "12114868"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[{datetime.now()}] Connected to MQTT Broker!")
        print(f"Publishing to topic: {TOPIC}")
    else:
        print(f"Failed to connect, return code {rc}")

def on_publish(client, userdata, mid):
    print(f"[{datetime.now()}] Message {mid} published")

# Create MQTT client
client = mqtt.Client(CLIENT_ID)
client.on_connect = on_connect
client.on_publish = on_publish

try:
    # Connect to broker
    client.connect(BROKER, PORT, 60)
    client.loop_start()
    
    print(f"\n{'='*60}")
    print(f"Temperature Sensor Publisher Started")
    print(f"Student ID: {STUDENT_ID}")
    print(f"{'='*60}\n")
    
    # Publish temperature data every 3 seconds
    count = 0
    while True:
        # Simulate temperature reading (20-35°C)
        temperature = round(random.uniform(20.0, 35.0), 2)
        
        # Create message payload
        payload = {
            "sensor_id": "TEMP_001",
            "student_id": STUDENT_ID,
            "temperature": temperature,
            "unit": "Celsius",
            "timestamp": datetime.now().isoformat(),
            "count": count
        }
        
        # Publish message
        result = client.publish(TOPIC, json.dumps(payload), qos=1)
        
        # Log to console and file
        log_msg = f"[{datetime.now()}] Published: {json.dumps(payload, indent=2)}"
        print(log_msg)
        
        with open("temperature_pub_log.txt", "a") as f:
            f.write(log_msg + "\n" + "-"*60 + "\n")
        
        count += 1
        time.sleep(3)
        
except KeyboardInterrupt:
    print("\n\nShutting down publisher...")
    client.loop_stop()
    client.disconnect()
    print("Publisher stopped.")