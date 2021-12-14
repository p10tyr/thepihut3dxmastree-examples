from gpiozero import LED
from time import sleep

CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

led = LED(2)


def dot():
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)


def dash():
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.2)


while True:
    input = input('What would you like to send? ')
    for letter in input:
        for symbol in CODE[letter.upper()]:
            if symbol == '-':
                dash()
            elif symbol == '.':
                dot()
            else:
                sleep(0.5)
        sleep(0.5)
    print("Message Sent!")
