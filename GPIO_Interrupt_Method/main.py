'''

Author: Michael Li
Date: 7/5/2019

Example: Detect white line

// Seeed line finder (grove interface)

// red   5V
// black gnd
// white NC
// yellow D3 (Output) (Hint: UNO input)

// D3 1 means black surface
//    0 means white line


'''


import json
import machine
import sys
import time
import utime
import ubinascii

from machine import Pin

blueled = machine.Pin(5, machine.Pin.OUT)

def handle_interrupt(pin):
    global blueled
    if pin.value() == 1:         
        blueled.value(1)
        print("Black Surface!")
    else:                           
        blueled.value(0)
        print("White Line!")




SAMPLING_TIME   = 1  # 5 seconds

print ("Setup: Pin 0 Exit, Pin 5 Blue Led, Pin 21 Line Sensor.")
# Pin definitions
repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

# Pin for the line finder sensor
pir = Pin(21, Pin.IN)     # create input pin on GPIO21
pir.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=handle_interrupt)
#pir.irq(trigger=3, handler=handle_interrupt)
'''
print ("Trigger mode:")
print (Pin.IRQ_RISING)  # 1
print (Pin.IRQ_FALLING) # 2
print (Pin.IRQ_RISING or Pin.IRQ_FALLING)  # 1 (true)
print (Pin.IRQ_RISING | Pin.IRQ_FALLING)   # 3 (0x01 | 0x02)
print (type(Pin.IRQ_RISING)) # int type
'''
# initialization
blueled.value(pir.value())

previous_time = utime.time()
time_min = 0

print ("Forever loop")
# Wait for button 0 to be pressed, and then exit
while True:
    #print ("Inside the loop")
    # If button 0 is pressed, drop to REPL
    if repl_button.value() == 0:
        print("Dropping to REPL now")
        sys.exit()
'''        
    current_time = utime.time()
    #print("current time : ")
    #print(current_time)
    #print("previous time : ")
    #print(previous_time)
    if (current_time - previous_time) > SAMPLING_TIME:
        previous_time = current_time
        if lineSensor.value() == 1:			
            blueled.value(1)
            print("Black Surface!")
        else:							
            blueled.value(0)
            print("White Line!")

'''