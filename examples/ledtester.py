from gpiozero import LED
from time import sleep

fields = [
    ("2", "LED 25 (star)", "3"),
    ("4", "LED 1", "7"),
    ("5", "LED 7", "29"),
    ("6", "LED 16", "31"),
    ("7", "LED 22", "26"),
    ("8", "LED 6", "24"),
    ("9", "LED 14", "21"),
    ("10", "LED 8", "19"),
    ("11", "LED 21", "23"),
    ("12", "LED 15", "32"),
    ("13", "LED 3", "33"),
    ("14", "LED 19", "8"),
    ("15", "LED 2", "10"),
    ("16", "LED 9", "36"),
    ("17", "LED 10", "11"),
    ("18", "LED 20", "12"),
    ("19", "LED 18", "35"),
    ("20", "LED 17", "38"),
    ("21", "LED 4", "40"),
    ("22", "LED 24", "15"),
    ("23", "LED 23", "16"),
    ("24", "LED 13", "18"),
    ("25", "LED 5", "22"),
    ("26", "LED 12", "37"),
    ("27", "LED 11", "13"),
]


for field in fields:
    x = field[0]
    led = LED(int(x))
    led.off()

print(('\x1b[4;37;40m' + "LED NO.        GPIO NO.  PIN NO." + '\x1b[0m'))

for field in fields:
    x = field[0]
    led = LED(int(x))
    led.on()
    print(('\x1b[0;32;40m' + "{} (On)     GPIO {:<4} Pin {:<4}".format(field[1],
          field[0], field[2]) + '\x1b[0m'))
    sleep(1)
    led.off()
    print(('\x1b[0;31;40m' + "{} (Off)    GPIO {:<4} Pin {:<4}".format(field[1],
          field[0], field[2]) + '\x1b[0m'))
    sleep(1)
