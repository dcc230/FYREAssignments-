# Team member names: Agragyan, Cristian, Dean
# Purpose of the code: Arm a light detection system that when enough daylight is detected it activates a servo to turn on a light switch in a room and turn it off when not enough is there
# Date code was started: 09/23/26
# Date of last update: 09/23/26
# Explanation of AI use: We used AI to write the whole thing

from machine import Pin, PWM
from time import sleep


# ==========================================
# PIN SETUP
# ==========================================

# Light sensor
sensor = Pin(7, Pin.IN)

# LED -> resistor -> GND
led = Pin(8, Pin.OUT)

# I/O switch -> GPIO 9
# Switch connects GPIO 9 to GND when ON
switch = Pin(9, Pin.IN, Pin.PULL_UP)

# Servo that turns light ON
servo_on = PWM(Pin(5), freq=50)

# Servo that turns light OFF
servo_off = PWM(Pin(6), freq=50)


# ==========================================
# SERVO FUNCTION
# ==========================================

def servo_angle(servo, angle):

    min_duty = 1638
    max_duty = 8192

    duty = int(
        min_duty +
        (angle / 180) * (max_duty - min_duty)
    )

    servo.duty_u16(duty)


# ==========================================
# TURN LIGHT ON
# ==========================================

def turn_light_on():

    print(">>> TURNING LIGHT ON")

    servo_angle(servo_on, 90)
    sleep(0.7)

    servo_angle(servo_on, 0)
    sleep(0.5)


# ==========================================
# TURN LIGHT OFF
# ==========================================

def turn_light_off():

    print(">>> TURNING LIGHT OFF")

    servo_angle(servo_off, 90)
    sleep(0.7)

    servo_angle(servo_off, 0)
    sleep(0.5)


# ==========================================
# VARIABLES
# ==========================================

armed = False
light_on = False


# ==========================================
# STARTUP
# ==========================================

led.value(0)

print("----------------------------------------")
print("       DAYLIGHT LIGHT CONTROLLER")
print("----------------------------------------")
print("SYSTEM DISARMED")
print("LED OFF")
print("----------------------------------------")


# ==========================================
# MAIN LOOP
# ==========================================

while True:

    # Read switch
    switch_state = switch.value()


    # ======================================
    # SWITCH = ON / I
    # ======================================

    if switch_state == 0:

        # Arm ONLY if we weren't already armed
        if not armed:

            armed = True
            led.value(1)

            print()
            print("==============================")
            print("       SYSTEM ARMED")
            print("==============================")
            print("LED ON")
            print("DAYLIGHT SENSOR ACTIVE")
            print()


        # ----------------------------------
        # SENSOR ONLY WORKS WHILE ARMED
        # ----------------------------------

        daylight = sensor.value()


        if daylight == 1:

            print("ARMED: ENOUGH DAYLIGHT")

            # If light is ON, turn it OFF
            if light_on:

                turn_light_off()
                light_on = False


        else:

            print("ARMED: NOT ENOUGH DAYLIGHT")

            # If light is OFF, turn it ON
            if not light_on:

                turn_light_on()
                light_on = True


    # ======================================
    # SWITCH = OFF / ON
    # ======================================

    else:

        # Disarm ONLY if currently armed
        if armed:

            armed = False
            led.value(0)

            print()
            print("==============================")
            print("      SYSTEM DISARMED")
            print("==============================")
            print("LED OFF")
            print("DAYLIGHT SENSOR INACTIVE")
            print()


        # Sensor is NOT read or used here
        print("DISARMED: SENSOR INACTIVE")


    sleep(0.5)
