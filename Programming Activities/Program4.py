# This program was created in Arduino Lab for MicroPython
#Blinking Program


#incorperate Modules
import machine #microcontroller stuff
import time 

#make LED object
led = machine.Pin(0,machine.Pin.OUT)
#infinite Loop
while True:
  led.value(1) #led on
  time.sleep(.5)
  led.value(0)
   time.sleep(.5)
  

  
