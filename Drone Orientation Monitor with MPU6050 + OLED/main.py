# ==========================================================
# Captr - AI Powered ESP32 Smart Motion & Health Monitor
# Hardware:
# ESP32
# PIR Motion Sensor
# MAX30102 Heart Rate & SpO2 Sensor (Placeholder)
# ECG Sensor
# Flex Sensor
# OLED SSD1306
# LED
# Push Button
#
# Developed using MicroPython
# ==========================================================

from machine import Pin, ADC, I2C
from time import sleep
from ssd1306 import SSD1306_I2C
import random

# -------------------------
# Pin Configuration
# -------------------------

PIR_PIN = 14
LED_PIN = 2
BUTTON_PIN = 12

FLEX_PIN = 34
ECG_PIN = 35

SDA_PIN = 21
SCL_PIN = 22

# -------------------------
# Initialize Hardware
# -------------------------

pir = Pin(PIR_PIN, Pin.IN)
led = Pin(LED_PIN, Pin.OUT)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

flex = ADC(Pin(FLEX_PIN))
flex.atten(ADC.ATTN_11DB)

ecg = ADC(Pin(ECG_PIN))
ecg.atten(ADC.ATTN_11DB)

i2c = I2C(0, scl=Pin(SCL_PIN), sda=Pin(SDA_PIN))

oled = SSD1306_I2C(128, 64, i2c)

# ==========================================================
# MAX30102 (Simulation)
# Replace with actual driver if available
# ==========================================================

def read_max30102():
    bpm = random.randint(65, 90)
    spo2 = random.randint(96, 100)
    return bpm, spo2

# ==========================================================
# AI Decision Engine
# ==========================================================

def ai_analysis(motion, bpm, spo2, ecg_value, flex_value):

    alerts = []

    if motion:
        alerts.append("Motion")

    if bpm < 60 or bpm > 100:
        alerts.append("Heart Rate")

    if spo2 < 95:
        alerts.append("Low SpO2")

    if ecg_value > 3000:
        alerts.append("ECG")

    if flex_value > 2500:
        alerts.append("Flex")

    return alerts

# ==========================================================
# OLED Display
# ==========================================================

def update_display(motion, bpm, spo2, ecg_value, flex_value):

    oled.fill(0)

    oled.text("Captr AI Device",0,0)
    oled.text("Motion:"+str(motion),0,12)
    oled.text("HR:"+str(bpm),0,24)
    oled.text("SpO2:"+str(spo2),0,36)
    oled.text("ECG:"+str(ecg_value),0,48)

    oled.show()

# ==========================================================
# Startup
# ==========================================================

print("====================================")
print("Captr AI Smart Monitoring Device")
print("System Boot Successful")
print("====================================")

# ==========================================================
# Main Loop
# ==========================================================

while True:

    # Read Sensors
    motion = pir.value()

    bpm, spo2 = read_max30102()

    ecg_value = ecg.read()

    flex_value = flex.read()

    button_state = not button.value()

    # AI Processing
    alerts = ai_analysis(
        motion,
        bpm,
        spo2,
        ecg_value,
        flex_value
    )

    # LED Alert
    if alerts:
        led.on()
    else:
        led.off()

    # OLED Display
    update_display(
        motion,
        bpm,
        spo2,
        ecg_value,
        flex_value
    )

    # Serial Monitor
    print("\n========== SENSOR DATA ==========")
    print("Motion      :", motion)
    print("Heart Rate  :", bpm, "BPM")
    print("SpO2        :", spo2, "%")
    print("ECG         :", ecg_value)
    print("Flex        :", flex_value)
    print("Button      :", button_state)
    print("AI Alerts   :", alerts)
    print("=================================\n")

    sleep(1)
