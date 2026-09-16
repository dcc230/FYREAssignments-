# Team member names: Agragyan, Cristian, Dean
# Purpose of the code: Move a servo 180 degrees when a button is held, then back when released
# Date code was started: 09/16/26
# Date of last update: 09/16/26
# Explanation of AI use: We used AI to write the whole thing

from machine import Pin, PWM
from time import sleep

# Button on GPIO 6
button = Pin(6, Pin.IN, Pin.PULL_UP)

# Servo on GPIO 5
servo = PWM(Pin(5), freq=50)

def set_servo_angle(angle):
    # Convert 0-180 degrees to servo duty cycle
    min_duty = 1638   # approximately 0.5 ms
    max_duty = 8192   # approximately 2.5 ms

    duty = min_duty + (max_duty - min_duty) * angle // 180
    servo.duty_u16(duty)

# Start at 0 degrees
set_servo_angle(0)

while True:
    if button.value() == 0:
        # Button pressed
        set_servo_angle(180)
    else:
        # Button released
        set_servo_angle(0)

    sleep(0.01)
