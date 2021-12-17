##
# Example code from The Pi Hut comments section by Dj
# "
#   Just the mapping of pins to LEDs....
#   I worked it out by hand (2's the star, 3's unknown) and put together this bit of code for a cascade of LEDs...
# "
# https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi
##

from gpiozero import LEDBoard
from time import sleep

treelights = [18, 5, 9, 11, 21, 10, 7, 12, 6, 1, 14,
              3, 20, 24, 13, 15, 2, 17, 16, 23, 8, 22, 4, 19]
treemap = {1: 4, 7: 5, 16: 6, 22: 7, 6: 8, 14: 9, 8: 10, 21: 11, 15: 12, 3: 13, 19: 14, 2: 15,
           9: 16, 10: 17, 20: 18, 18: 19, 17: 20, 4: 21, 24: 22, 23: 23, 13: 24, 5: 25, 12: 26, 11: 27}

leds = LEDBoard(*list(range(4, 28)), pwm=True)


def labelToPin(label):
    return treemap[label]


def toBoard(label):
    return labelToPin(label)-4


while True:
    for i in treelights:
        sleep(0.1)
        leds.on(toBoard(i))

    for i in treelights:
        sleep(0.1)
        leds.off(toBoard(i))
