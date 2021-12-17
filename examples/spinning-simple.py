##
# A simple spinning code example
#
##

import time
from gpiozero import LEDBoard
from gpiozero.tools import random_values

speed = 0.5

east = LEDBoard(16, 13, 20, 19, 26, 21, pwm=True)
south = LEDBoard(25, 24, 23, 9, 22, 10, pwm=True)
west = LEDBoard(17, 4, 14, 27, 18, 15, pwm=True)
north = LEDBoard(8, 6, 7, 11, 5, 12, pwm=True)

while True:
    south.off()
    north.on()
    time.sleep(speed)

    west.off()
    east.on()
    time.sleep(speed)

    north.off()
    south.on()
    time.sleep(speed)

    east.off()
    west.on()
    time.sleep(speed)
