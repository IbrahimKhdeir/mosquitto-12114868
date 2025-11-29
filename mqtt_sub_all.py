import paho.mqtt.client as mqtt
import json
from datetime import datetime

# MQTT Broker Configuration
BROKER = "localhost"
PORT = 1883
TOPICS = [
    ("sensors/temperature", 1),
    ("sensors/humidity", 1),
    ("sensors/people_counter", 1)
]
CLIENT_ID = "all_sensors_subscriber"

# Student ID
STUDENT_ID = "12114868"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[{datetime.now()}] Connected to MQTT Broker!")
        print("Subscribing to multiple topics:")
        for topic, qos in TOPICS:
            client.subscribe(topic, qos)
            print(f"  - {topic}")
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        # Parse JSON payload
        payload = json.loads(msg.payload.decode())
        
        # Determine message type based on topic
        topic_type = msg.topic.split('/')[-1]
        
        # Format received message
        log_msg = f"""
{'='*60}
[{datetime.now()}] Message Received
Topic: {msg.topic}
Type: {topic_type.upper()}
Student ID: {payload.get('student_id')}
Data: {json.dumps(payload, indent=2)}
{'='*60}
"""
        
        # Print to console
        print(log_msg)
        
        # Log to file
        with open("all_sensors_sub_log.txt", "a") as f:
            f.write(log_msg + "\n")
                
    except Exception as e:
        print(f"Error processing message: {e}")

# Create MQTT client
client = mqtt.Client(CLIENT_ID)
client.on_connect = on_connect
client.on_message = on_message

try:
    print(f"\n{'='*60}")
    print(f"All Sensors Subscriber Started")
    print(f"Student ID: {STUDENT_ID}")
    print(f"Monitoring all sensor topics...")
    print(f"{'='*60}\n")
    
    # Connect to broker
    client.connect(BROKER, PORT, 60)
    
    # Start loop to process received messages
    client.loop_forever()
    
except KeyboardInterrupt:
    print("\n\nShutting down subscriber...")
    client.disconnect()
    print("Subscriber stopped.")