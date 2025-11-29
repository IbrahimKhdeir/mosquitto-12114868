import paho.mqtt.client as mqtt
import json
from datetime import datetime

# MQTT Broker Configuration
BROKER = "localhost"
PORT = 1883
TOPIC = "sensors/people_counter"
CLIENT_ID = "people_counter_subscriber"

# Student ID
STUDENT_ID = "12114868"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[{datetime.now()}] Connected to MQTT Broker!")
        print(f"Subscribed to topic: {TOPIC}")
        client.subscribe(TOPIC, qos=1)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        # Parse JSON payload
        payload = json.loads(msg.payload.decode())
        
        # Format received message
        log_msg = f"""
{'='*60}
[{datetime.now()}] Message Received from Topic: {msg.topic}
Sensor ID: {payload.get('sensor_id')}
Student ID: {payload.get('student_id')}
People Detected: {payload.get('people_detected')}
Total Count: {payload.get('total_count')}
Location: {payload.get('location')}
Timestamp: {payload.get('timestamp')}
Message Count: {payload.get('count')}
{'='*60}
"""
        
        # Print to console
        print(log_msg)
        
        # Log to file
        with open("people_counter_sub_log.txt", "a") as f:
            f.write(log_msg + "\n")
        
        # Alert if too many people detected
        people = payload.get('people_detected', 0)
        if people > 10:
            alert = f"⚠️  CROWDED AREA ALERT: {people} people detected!"
            print(alert)
            with open("people_counter_sub_log.txt", "a") as f:
                f.write(alert + "\n\n")
                
    except Exception as e:
        print(f"Error processing message: {e}")

# Create MQTT client
client = mqtt.Client(CLIENT_ID)
client.on_connect = on_connect
client.on_message = on_message

try:
    print(f"\n{'='*60}")
    print(f"People Counter Subscriber Started")
    print(f"Student ID: {STUDENT_ID}")
    print(f"Waiting for messages...")
    print(f"{'='*60}\n")
    
    # Connect to broker
    client.connect(BROKER, PORT, 60)
    
    # Start loop to process received messages
    client.loop_forever()
    
except KeyboardInterrupt:
    print("\n\nShutting down subscriber...")
    client.disconnect()
    print("Subscriber stopped.")