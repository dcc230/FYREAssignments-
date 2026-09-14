from machine import Pin
from time import sleep

# Pins
button = Pin(6, Pin.IN, Pin.PULL_UP)
sensor = Pin(5, Pin.IN)
green_led = Pin(47, Pin.OUT)

# Start disarmed
armed = False
green_led.off()

while True:

    # Press button to arm
    if button.value() == 0:
        armed = True
        sleep(0.2)  # debounce

    # Green LED stays on once armed
    if sensor.value() == 1 and armed:
        green_led.on()
        # Check sensor
        print("INTRUDER DETECTED!")

    else:
        green_led.off()

    sleep(0.05)
