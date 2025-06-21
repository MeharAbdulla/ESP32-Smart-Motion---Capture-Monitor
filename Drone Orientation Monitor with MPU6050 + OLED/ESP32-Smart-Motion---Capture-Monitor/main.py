from machine import Pin, I2C
from time import sleep
import ssd1306

# OLED setup
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Pins
pir = Pin(12, Pin.IN)
button = Pin(14, Pin.IN, Pin.PULL_UP)  # PULL_UP enabled
led = Pin(13, Pin.OUT)

def show_message(msg):
    oled.fill(0)
    oled.text(msg, 0, 25)
    oled.show()

# Start
show_message("System Ready")
led.value(0)

while True:
    if pir.value():  # PIR motion detected
        show_message("Face Detected")
        led.value(1)
        sleep(1)
        led.value(0)

    elif button.value() == 0:  # Button pressed
        show_message("Capturing...")
        led.value(1)
        sleep(1)
        show_message("Done!")
        sleep(1)
        led.value(0)  # Turn off LED after Done

    else:
        show_message("Monitoring...")
        led.value(0)

    sleep(0.1)
