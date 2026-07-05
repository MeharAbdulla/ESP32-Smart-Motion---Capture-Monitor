# Captr – AI-Powered ESP32 Smart Motion & Health Monitoring Device

## 📖 Overview

**Captr** is an AI-powered smart monitoring device built with **ESP32** and **MicroPython**. It combines motion detection and real-time health monitoring by integrating multiple sensors into a compact embedded system. The device continuously monitors environmental activity and physiological data while displaying live information on an OLED screen and providing visual alerts.

Designed for IoT, embedded systems, and AI-based monitoring applications, Captr demonstrates intelligent sensor fusion, real-time processing, and predictive analytics on resource-constrained hardware.

---

## ✨ Features

* 🤖 AI-powered smart monitoring
* 🚶 PIR motion detection
* ❤️ Heart rate and SpO₂ monitoring (MAX30102)
* 📈 ECG signal monitoring
* ✋ Flex sensor gesture/bend detection
* 📺 OLED real-time display
* 💡 LED alert notifications
* 🔘 Button-controlled operations
* ⚡ Real-time sensor processing
* 🧠 Intelligent data analysis
* 📊 Predictive analytics
* 📡 Embedded IoT architecture
* 🐍 Developed using MicroPython

---

## 🛠️ Hardware Components

* ESP32 Development Board
* PIR Motion Sensor
* MAX30102 Pulse Oximeter & Heart Rate Sensor
* ECG Sensor Module
* Flex Sensor
* OLED Display (I2C)
* Push Button
* LED
* Breadboard & Jumper Wires
* USB Cable

---

## 💻 Software & Technologies

* MicroPython
* ESP32
* Embedded Systems
* IoT
* I2C Communication
* GPIO Programming
* Sensor Fusion
* Real-Time Data Processing
* AI-Based Monitoring

---

## 🧠 AI Techniques

* Intelligent Sensor Fusion
* Real-Time Data Processing
* Pattern Recognition
* Predictive Analytics
* Health Monitoring
* Motion Detection
* Rule-Based Decision Making
* Event Detection
* Smart Alert Generation
* Embedded AI Concepts

---

## 📂 Project Structure

```text
Captr/
│── main.py
│── boot.py
│── max30102.py
│── ecg.py
│── flex.py
│── pir.py
│── oled.py
│── config.py
│── utils.py
│── README.md
```

---

## ⚙️ System Workflow

1. Initialize ESP32 and peripherals.
2. Read data from the PIR motion sensor.
3. Monitor heart rate and SpO₂ using the MAX30102.
4. Capture ECG readings.
5. Detect finger movement using the flex sensor.
6. Process sensor data in real time.
7. Display system status on the OLED.
8. Trigger LED alerts when predefined conditions are met.
9. Perform AI-inspired analysis for smart monitoring.

---

## 🚀 Installation

1. Flash **MicroPython** onto the ESP32.
2. Clone this repository.

```bash
git clone https://github.com/your-username/Captr.git
```

3. Upload all project files to the ESP32.
4. Connect the sensors according to the wiring diagram.
5. Run:

```python
main.py
```

---

## 📊 Applications

* Smart Health Monitoring
* Wearable Device Prototypes
* Motion Detection Systems
* Home Automation
* IoT Projects
* Embedded AI Research
* Remote Patient Monitoring
* Biomedical Signal Analysis
* Smart Safety Systems

---

## 🎯 Future Improvements

* Cloud integration
* Mobile application support
* Wi-Fi dashboard
* MQTT communication
* Machine learning-based anomaly detection
* Health history logging
* SMS and email alerts
* Voice assistant integration
* Battery optimization

---

## 👨‍💻 Author

Developed as an AI-powered Embedded Systems and IoT project using **ESP32**, **MicroPython**, and intelligent sensing technologies.

---

## 📄 License

This project is released under the **MIT License**. Feel free to use, modify, and distribute it for educational and research purposes.
