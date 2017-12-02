##
# Run this code to  step through each GPIO to find the LED on the tree
# 1- Turns off all LED
#
# Press enter to loop through and turn on the next GPIO while the previous one gets turned off
##

import time
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
tree = LEDBoard(*range(2,28),pwm=True)

print "All OFF"
tree.off()
raw_input("Press Enter for Next")

for led in tree:
    print "LED "+ str(led.pin) +  " - ON"
    led.on()
    raw_input("Press Enter for Next")
    led.off()
