##
#
# Code provided by Kjetil from the comments section from The Pi Hut
# "
# For me, the example code only lit up a single LED and didn't do much more. I adopted it into something that seems to work better (for me):
# " 
#
# https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi
#
##

from gpiozero import LEDBoard 
from gpiozero.tools import random_values 
from time import sleep 
tree = LEDBoard(*range(2,28),pwm=True) 
while True: 
  for led in tree: 
    led.source_delay = 2 
    led.source = random_values() 
    sleep(5)
