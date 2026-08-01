# 🌱 IoT Smart Irrigation System using ESP32 & MicroPython

![ESP32](https://img.shields.io/badge/ESP32-IoT-blue)
![MicroPython](https://img.shields.io/badge/MicroPython-3.0-green)
![Blynk](https://img.shields.io/badge/Blynk-Cloud-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

An IoT-based Smart Irrigation System designed to automate irrigation using an ESP32 microcontroller, soil moisture sensor, and Blynk Cloud. The system continuously monitors soil moisture and automatically controls a water pump while enabling remote monitoring and manual control through the Blynk mobile application.

---

# 📖 Project Overview

Water scarcity has become one of the biggest challenges in modern agriculture. Traditional irrigation methods often lead to water wastage due to manual operation and lack of continuous monitoring.

This project provides an intelligent irrigation solution capable of:

- Monitoring soil moisture continuously
- Automatically controlling the water pump
- Displaying live moisture data
- Manual pump control from anywhere
- Wireless monitoring through Wi-Fi

The project is implemented using ESP32 and MicroPython, making it inexpensive, scalable, and easy to deploy.

---

# 🚀 Features

✔ Automatic Irrigation

✔ Real-Time Soil Moisture Monitoring

✔ Remote Pump Control

✔ Wi-Fi Connectivity

✔ MQTT Communication

✔ Blynk Cloud Integration

✔ Automatic Moisture Alerts

✔ Low Cost

✔ Energy Efficient

✔ Easy to Expand

---

# 💻 Firmware Versions
| Version     | Language | IDE         | Status |
| ----------- | -------- | ----------- | ------ |
| Arduino     | C++      | Arduino IDE | ✅     |
| MicroPython | Python   | Thonny IDE  | ✅     |

This project is available in two firmware implementations:

- Arduino IDE (C++) using the ESP32 Arduino core.
- MicroPython using Thonny IDE.

Both versions provide the same functionality, allowing users to choose the development environment they prefer.

---

# 🛠 Hardware Used

| Component | Quantity |
|-----------|---------|
| ESP32 Development Board | 1 |
| Soil Moisture Sensor | 1 |
| Relay Module | 1 |
| Water Pump | 1 |
| Breadboard | 1 |
| Jumper Wires | Several |
| Power Supply | 1 |

---

# 💻 Software Used

- MicroPython
- Thonny IDE
- Blynk IoT Cloud
- MQTT Protocol

---

# ⚙ Working Principle

1. ESP32 connects to Wi-Fi.
2. Soil moisture is measured.
3. Moisture percentage is calculated.
4. Data is uploaded to Blynk Cloud.
5. If soil moisture falls below the threshold:
   - Pump automatically turns ON.
6. When soil becomes sufficiently wet:
   - Pump turns OFF.
7. User can also manually control the pump using the Blynk application.

---

# 📡 System Architecture

ESP32

↓

Soil Moisture Sensor

↓

MicroPython Program

↓

Decision Logic

↓

Relay

↓

Water Pump

↓

Blynk Cloud

↓

Mobile App

---

# 📷 Project Images

<img width="2048" height="1156" alt="implementation" src="https://github.com/user-attachments/assets/8a91cd00-079a-4eca-87f4-75c5d3f18367" />

---
# ▶ Running the Project

Clone the repository

```bash
git clone https://github.com/yourusername/IoT-Smart-Irrigation-System.git
```

Open using Thonny IDE.

Install MicroPython firmware on ESP32.

Update:

```python
WIFI_SSID
WIFI_PASSWORD
BLYNK_AUTH_TOKEN
```

Run

```text
smart_irrigation.py
```

---

# 📈 Future Improvements

- Weather API Integration
- Multiple Soil Sensors
- Solar Powered System
- Water Level Monitoring
- Mobile Notifications
- AI-based Irrigation Prediction

---

# 📜 License

MIT License

---

# 👨‍💻 Author

Chinmay Yalawatti

Electronics & Communication Engineering

ESP32 | IoT | Embedded Systems | MicroPython
