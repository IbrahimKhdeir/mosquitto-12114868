import paho.mqtt.client as mqtt
import time
import random
import json
from datetime import datetime

# MQTT Broker Configuration
BROKER = "localhost"
PORT = 1883
TOPIC = "sensors/humidity"
CLIENT_ID = "humidity_publisher"

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
    print(f"Humidity Sensor Publisher Started")
    print(f"Student ID: {STUDENT_ID}")
    print(f"{'='*60}\n")
    
    # Publish humidity data every 4 seconds
    count = 0
    while True:
        # Simulate humidity reading (30-90%)
        humidity = round(random.uniform(30.0, 90.0), 2)
        
        # Create message payload
        payload = {
            "sensor_id": "HUM_001",
            "student_id": STUDENT_ID,
            "humidity": humidity,
            "unit": "Percent",
            "timestamp": datetime.now().isoformat(),
            "count": count
        }
        
        # Publish message
        result = client.publish(TOPIC, json.dumps(payload), qos=1)
        
        # Log to console and file
        log_msg = f"[{datetime.now()}] Published: {json.dumps(payload, indent=2)}"
        print(log_msg)
        
        with open("humidity_pub_log.txt", "a") as f:
            f.write(log_msg + "\n" + "-"*60 + "\n")
        
        count += 1
        time.sleep(4)
        
except KeyboardInterrupt:
    print("\n\nShutting down publisher...")
    client.loop_stop()
    client.disconnect()
    print("Publisher stopped.")