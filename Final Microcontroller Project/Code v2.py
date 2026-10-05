from machine import Pin, PWM, ADC
from time import sleep


# ==========================================
# PIN SETUP
# ==========================================

# ------------------------------------------
# DAYLIGHT SENSOR
# ------------------------------------------

sensor = Pin(7, Pin.IN)


# ------------------------------------------
# ORIGINAL LED
# ------------------------------------------

led = Pin(8, Pin.OUT)


# ------------------------------------------
# ARMING SWITCH
# ------------------------------------------

# I/O switch -> GPIO 9
# Switch connects GPIO 9 to GND when ON

switch = Pin(9, Pin.IN, Pin.PULL_UP)


# ------------------------------------------
# SERVO
# ------------------------------------------

servo_on = PWM(Pin(5), freq=50)


# ------------------------------------------
# RAIN SENSOR
# ------------------------------------------

rain_sensor = ADC(Pin(1))


# ------------------------------------------
# RAIN LED
# ------------------------------------------

rain_led = Pin(2, Pin.OUT)


# ==========================================
# RESET SYSTEM AT STARTUP
# ==========================================

# Turn ALL LEDs OFF
led.value(0)
rain_led.value(0)

# Put servo at OFF/resting position
# The servo will stay here until the
# daylight system tells it to move.
servo_on.duty_u16(1638)

print("----------------------------------------")
print("       SYSTEM RESET")
print("----------------------------------------")
print("DAYLIGHT LED: OFF")
print("RAIN LED: OFF")
print("SERVO: OFF POSITION")
print("----------------------------------------")


# ==========================================
# RAIN SENSOR SETTINGS
# ==========================================

RAIN_THRESHOLD = 60


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

    sleep(0.3)


# ==========================================
# TURN LIGHT OFF
# ==========================================

def turn_light_off():

    print(">>> TURNING LIGHT OFF")

    servo_angle(servo_on, 90)

    sleep(0.3)

    servo_angle(servo_on, 0)

    sleep(0.3)


# ==========================================
# VARIABLES
# ==========================================

armed = False
light_on = False


# ==========================================
# STARTUP
# ==========================================

print("----------------------------------------")
print("       DAYLIGHT LIGHT CONTROLLER")
print("----------------------------------------")
print("SYSTEM DISARMED")
print("DAYLIGHT LED OFF")
print("RAIN SENSOR ACTIVE")
print("RAIN SENSOR = GPIO 1")
print("RAIN LED = GPIO 2")
print("RAIN THRESHOLD =", RAIN_THRESHOLD)
print("----------------------------------------")


# ==========================================
# MAIN LOOP
# ==========================================

while True:

    # ======================================
    # RAIN SENSOR
    # ======================================

    rain_value = rain_sensor.read_uv()
    rknown=330
    rain_value=rknown*((rain_value/1000.0)/(3300-(rain_value/1000)))
    print("RAIN SENSOR VALUE:", rain_value)


    if rain_value > RAIN_THRESHOLD:

        # RAIN DETECTED
        rain_led.value(0)

        print(">>> RAIN / MOISTURE DETECTED")
        print(">>> RAIN LED ON")

    else:

        # NO RAIN
        rain_led.value(1)

        print(">>> NO RAIN")
        print(">>> RAIN LED OFF")


    # ======================================
    # READ ARMING SWITCH
    # ======================================

    switch_state = switch.value()


    # ======================================
    # SWITCH ON
    # ======================================

    if switch_state == 0:

        if not armed:

            armed = True

            led.value(1)
            servo_angle(servo_on, 90)
            print()
            print("==============================")
            print("       SYSTEM ARMED")
            print("==============================")
            print("LED ON")
            print("DAYLIGHT SENSOR ACTIVE")
            print()


        # ==================================
        # DAYLIGHT SENSOR
        # ==================================

        daylight = sensor.value()


        # ----------------------------------
        # ENOUGH DAYLIGHT
        # ----------------------------------

        if daylight == 1:

            print("ARMED: ENOUGH DAYLIGHT")

            if light_on:

                turn_light_off()

                light_on = False


        # ----------------------------------
        # NOT ENOUGH DAYLIGHT
        # ----------------------------------

        else:

            print("ARMED: NOT ENOUGH DAYLIGHT")

            if not light_on:

                turn_light_on()

                light_on = True


    # ======================================
    # SWITCH OFF
    # ======================================

    else:

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
            servo_angle(servo_on, 0)


        print("DISARMED: SENSOR INACTIVE")


    # ======================================
    # LOOP DELAY
    # ======================================

    sleep(0.3)
