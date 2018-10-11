from time import sleep
import keyboard

morse = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
      	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

def morsify(length = 0.2):
    msg = input('MESSAGE: ')
    msg_morse = ''
    for char in msg:
        if char is not ' ':
            msg_morse += (morse[char.upper()]+'/')
        else:
            msg_morse += ('/')
    msg_morse = msg_morse.split('//')
    for i in range(len(msg_morse)):
        for j in range(len(msg_morse[i])):
            if msg_morse[i][j] is '.':
                sleep(length)
                keyboard.press_and_release('Caps Lock')
                sleep(length)
                keyboard.press_and_release('Caps Lock')
            elif msg_morse[i][j] is '-':
                sleep(length)
                keyboard.press_and_release('Caps Lock')
                sleep(length*3)
                keyboard.press_and_release('Caps Lock')
            elif msg_morse[i][j] is '/':
                sleep(length*3)
        sleep(length*5)
    return msg_morse,
