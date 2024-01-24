# Slowly fades all LEDs in and out. I can't remember if I saw this somewhere else, since it was a year ago that I set it up.

from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
tree = LEDBoard(*range(2,28),pwm=True)
tree.on()
for led in tree:
        led.source_delay = 0.5
        led.pulse(fade_in_time=2, fade_out_time=2)
pause()
