# IoT Sensor System using MQTT (Mosquitto + Python Paho)

**Student ID:** 12114868  
**Course:** IoT & Embedded Systems  
**Project:** MQTT Multi-Sensor Data Streaming  
**Date:** 29/11/2025  

---

## 📡 System Overview

This project demonstrates a real-time IoT messaging system using:

- MQTT Broker: Mosquitto  
- Protocol: MQTT  
- Programming Language: Python  
- Libraries: paho-mqtt  
- Communication Mode: Publish/Subscribe  

Multiple publishers send simulated sensor data, while multiple subscribers listen to specific topics or all topics.

---

## 🕸️ MQTT Topics Used

| Sensor | Topic |
|--------|------|
| Temperature | sensors/temperature |
| Humidity | sensors/humidity |
| People Counter | sensors/people_counter |

---

## 🧪 Sensors Implemented

### 1️⃣ Temperature Sensor
- Simulated temperature values from 20°C–35°C  
- Publishes every 3 seconds  
- Raises alert if temperature exceeds 30°C

### 2️⃣ Humidity Sensor
- Simulated humidity between 30%–90%  
- Publishes every 4 seconds  
- Alerts on low or high humidity  

### 3️⃣ People Counter
- Measures number of detected people (0–15 range per iteration)  
- Tracks total number of people  
- Publishes every 5 seconds  

---

## 📥 Subscribers

### Specific subscribers:
- mqtt_sub_temp.py → sensors/temperature  
- mqtt_sub_humidity.py → sensors/humidity  
- mqtt_sub_counter.py → sensors/people_counter  

### Multi-topic subscriber:
- mqtt_sub_all.py subscribes to:  
  sensors/temperature  
  sensors/humidity  
  sensors/people_counter  

---

## 🔧 Installation & Setup

### 1. Install Mosquitto  
Windows:  
mosquitto -v



---

### 2. Install Paho MQTT for Python  
py -3.12 -m pip install paho-mqtt==1.6.1



---

### 3. Run subscribers first  

py -3.12 mqtt_sub_temp.py
py -3.12 mqtt_sub_humidity.py
py -3.12 mqtt_sub_counter.py
py -3.12 mqtt_sub_all.py




---

### 4. Then run publishers  

py -3.12 mqtt_pub_temp.py
py -3.12 mqtt_pub_humidity.py
py -3.12 mqtt_pub_counter.py



---

## 🧩 Example JSON Message  
{
"sensor_id": "TEMP_001",
"student_id": "12114868",
"temperature": 28.24,
"unit": "Celsius",
"timestamp": "2025-11-29T17:04:39.898440",
"count": 87
}




---

## ⚠️ Alerts  
- Temperature > 30°C → HIGH TEMPERATURE ALERT  
- Humidity > 70% → HIGH HUMIDITY ALERT  
- Humidity < 40% → LOW HUMIDITY ALERT  
- People detected > 10 → CROWDED AREA ALERT  

---

## 🖼️ Screenshots Included

### Temperature Publisher
<img width="919" height="529" alt="image" src="https://github.com/user-attachments/assets/f58bc327-0f7d-4718-9c91-556ab25be06e" />


### Temperature Subscriber
<img width="918" height="518" alt="image" src="https://github.com/user-attachments/assets/2ab79aa8-f8f2-424c-9752-25603e8a8819" />


### Humidity Publisher
<img width="939" height="514" alt="image" src="https://github.com/user-attachments/assets/a9ab3744-ce6b-4be8-bd74-9801701b36ac" />


### Humidity Subscriber
<img width="917" height="537" alt="image" src="https://github.com/user-attachments/assets/66a2f4ac-0348-4b30-ac74-e6a84e2d1e66" />


### People Counter Publisher
<img width="921" height="530" alt="image" src="https://github.com/user-attachments/assets/f950f7ea-ab17-43c6-b2a1-fde68446df9e" />


### People Counter Subscriber
<img width="923" height="525" alt="image" src="https://github.com/user-attachments/assets/264e17e3-20b7-4600-a83e-e0fa1ff1169e" />


### Multi-topic Subscriber
<img width="1116" height="630" alt="image" src="https://github.com/user-attachments/assets/dd106f01-4105-480f-b150-7cd9db95596e" />


---

## 🧾 Log Files

- temperature_pub_log.txt  
- temperature_sub_log.txt  
- humidity_pub_log.txt  
- humidity_sub_log.txt  
- people_counter_pub_log.txt  
- people_counter_sub_log.txt  
- all_sensors_sub_log.txt  

---

## Final Result ✔

This IoT project successfully demonstrates:
- Real-time sensor data streaming using MQTT  
- Multiple publishers & subscribers  
- Topic-based message routing  
- JSON payload formatting  
- Log file storage  
- Functional alert system  
- Verified real execution  
- Student ID included in every data packet  

---

## Conclusion 🙌

System works fully as intended and completes all project requirements.  
The concept of distributed IoT data messaging with MQTT is implemented in a clear and practical way.
