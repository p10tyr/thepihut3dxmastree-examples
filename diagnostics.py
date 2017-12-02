##
# Run this code to check if all your LEDs are working
# 1- Tests each LED in a loop
# 2- Turns all LEDs off
# 3- Turns all LEDs on
# 3- Fades in and out using PWN (gpizero api)
##

import time
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
tree = LEDBoard(*range(2,28),pwm=True)

print "DIAG_XMAS   - Tree diagnostics terminal..."


print "DIAG_X_001 - Loop all LEDs ON"
for led in tree:
    print "DIAG_X_003 - LED "+ str(led.pin) +  " - ON"
    led.on()
    time.sleep(1)

print "DIAG_X_002 - All LEDs OFF"
tree.off()
time.sleep(1)

print "DIAG_X_003 - All LEDs ON"
tree.on()
time.sleep(3)    

print "DIAG_X_004 - All LEDs Fade on and off 3 times with PWN"
tree.off()
tree.pulse(1,1,3,False)

print "DIAG_XMAS  - Diagnostics Complete. Merry XMAS!"