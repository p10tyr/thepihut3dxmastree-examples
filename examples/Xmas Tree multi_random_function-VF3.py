#!/usr/bin/env python
# Program for the Pi Hut Xmas Tree
# that does multiple patterns in a random order
#
# Glyn Morgan 
# Version: Final-3 02/12/17
#
# Needs the GPIO Zero Library
#
# The PI Hut Xmas tree board is optionaly modified with a
# button between the otherwise unused GPIO3 & ground.
# This is to provide a clean shutdown method when used
# in a stand-alone mode.
# The button is wired between pins 5 & 6 of the GPIO
# connector on the tree.
#
# It can take a while for the program to spot that
# the shutdown button has been pushed. So hold the button
# in until the light sequence stops.

from gpiozero import LEDBoard
from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import Button
from subprocess import check_call
from gpiozero.tools import random_values
from random import *
import time

# set up various delay values
delay = 0.05    #used in spiral function
delay2 = 0.03   #used in spiral function
on_delay = 0.01 #used in random_led function
top_down_delay = 0.125 # used in top_down function
top_down_delay2 = 0.05 # used in top_down function
sides_delay = 0.075 # used in the sides function

# Just flicker the star led
star = PWMLED(2)
star.source = random_values()

# define the shutdown sequence for the shutdown button
def shutdown():
    check_call(['sudo', 'poweroff'])

shutdown_btn = Button(3)

period_min = 3  # base number of seconds for each function
period_max = 10 # maximum number of seconds for each function


def spiral():
    # function to create a spiral pattern that repeats for a while

    branch1_leds = LEDBoard(27,17,4,18,15,14)
    branch2_leds = LEDBoard(11,5,8,12,6,7)
    branch3_leds = LEDBoard(19,16,26,13,20,21)
    branch4_leds = LEDBoard(25,9,22,24,23,10)
    
    branch1_leds.off()
    branch2_leds.off()
    branch3_leds.off()
    branch4_leds.off()
    time.sleep(delay)
    
    spiral_time = time.time() + uniform(period_min, period_max)

    while spiral_time > time.time():
        # spiral down
        for point in range(6):
            branch1_leds[point].on()
            time.sleep(delay2)
            branch2_leds[point].on()
            time.sleep(delay2)
            branch3_leds[point].on()
            time.sleep(delay2)
            branch4_leds[point].on()
            time.sleep(delay2)
  
        time.sleep(delay)
        
        # spiral up
        for point in range(5, -1, -1):
            branch1_leds[point].off()
            time.sleep(delay2)
            branch2_leds[point].off()
            time.sleep(delay2)
            branch3_leds[point].off()
            time.sleep(delay2)
            branch4_leds[point].off()
            time.sleep(delay2)
        
        time.sleep(delay)

def random_led():
    # function that turns off and on random leds

    tree = LEDBoard(*range(4,28))

    random_time = time.time() + uniform(period_min, period_max)

    while random_time > time.time():
        
        # Turn on a random led
        on_lamp = randint(0, 23)
        tree[on_lamp].on()
        time.sleep(on_delay)

        # Turn off a random led
        off_lamp = randint(0, 23)
        tree[off_lamp].off()

   
def top_down(forward):
    # function that lights the leds from top down.
    # Or from bottom up if forward is not True.
 
    branch1_leds = LEDBoard(27,17,4,18,15,14)
    branch2_leds = LEDBoard(11,5,8,12,6,7)
    branch3_leds = LEDBoard(19,16,26,13,20,21)
    branch4_leds = LEDBoard(25,9,22,24,23,10)
    
    top_down_time = time.time()  + uniform(period_min, period_max)

    while top_down_time > time.time():
        branch1_leds.off()
        branch2_leds.off()
        branch3_leds.off()
        branch4_leds.off()
        time.sleep(top_down_delay2)

        if forward:
            for point in range(6):
                branch1_leds[point].on()
                branch2_leds[point].on()
                branch3_leds[point].on()
                branch4_leds[point].on()
                time.sleep(top_down_delay)                
        else:
            for point in range(5, -1, -1):
                branch1_leds[point].on()
                branch2_leds[point].on()
                branch3_leds[point].on()
                branch4_leds[point].on()
                time.sleep(top_down_delay)
     
 
def sides(forward):
    # function that lights the leds on the sides in sequence
    # direction is defined by forward being True or False
 
    side1_leds = LEDBoard(8,6,7)
    side2_leds = LEDBoard(11,5,12)
    side3_leds = LEDBoard(19,26,21)
    side4_leds = LEDBoard(16,13,20)
    side5_leds = LEDBoard(25,24,23)
    side6_leds = LEDBoard(9,22,10)
    side7_leds = LEDBoard(17,4,14)
    side8_leds = LEDBoard(27,18,15)
   
   
    sides_time = time.time() + uniform(period_min, period_max)

    while sides_time > time.time():
        if forward:
            # spin the side leds anticlockwise
            side1_leds.on()
            time.sleep(sides_delay)
            side1_leds.off()
            side2_leds.on()
            time.sleep(sides_delay)
            side2_leds.off()
            side3_leds.on()
            time.sleep(sides_delay)
            side3_leds.off()
            side4_leds.on()
            time.sleep(sides_delay)
            side4_leds.off()
            side5_leds.on()
            time.sleep(sides_delay)
            side5_leds.off()
            side6_leds.on()
            time.sleep(sides_delay)
            side6_leds.off()
            side7_leds.on()
            time.sleep(sides_delay)
            side7_leds.off()
            side8_leds.on()
            time.sleep(sides_delay)
            side8_leds.off()
        else:
            # spin the side leds clockwise
            side8_leds.on()
            time.sleep(sides_delay)
            side8_leds.off()
            side7_leds.on()
            time.sleep(sides_delay)
            side7_leds.off()
            side6_leds.on()
            time.sleep(sides_delay)
            side6_leds.off()
            side5_leds.on()
            time.sleep(sides_delay)
            side5_leds.off()
            side4_leds.on()
            time.sleep(sides_delay)
            side4_leds.off()
            side3_leds.on()
            time.sleep(sides_delay)
            side3_leds.off()
            side2_leds.on()
            time.sleep(sides_delay)
            side2_leds.off()
            side1_leds.on()
            time.sleep(sides_delay)
            side1_leds.off()

# Main Loop
old_sequence = 0
while True:
    # Pick a random sequence
    sequence = randint(1, 6)
    
    # test to stop doing the same sequence back to back
    if sequence != old_sequence:
        old_sequence = sequence
        
        if sequence == 1:
            random_led()
        elif sequence == 2:    
            spiral()
        elif sequence == 3:
            sides(True)     # flash sides anti clockwise
        elif sequence == 4:
            sides(False)    # flash sides clockwise
        elif sequence == 5:
            top_down(True)  # go top down           
        else:    
            top_down(False) # go bottom up

    # Test for a shutdown request
    if shutdown_btn.is_pressed:
        shutdown()
        
    
 






