import sys
from tkinter import *

import tkinter.font
from gpiozero import LED
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = LED(18)

win = Tk()
word = StringVar()

win.geometry('450x450+500+300')
win.title('Morse Code')

def Mcode():
    try:
        mtext = word.get()
        if len(mtext) > 12:
            mlabel = Label(win, text = 'Word is too long').pack()
        else:
            for i in mtext:
                for j in code[i.lower()]:
                    if j == '.':
                        dot()
                        mlabel = Label(win, text = j).pack()
                    elif j == '-':
                        dash()
                        mlabel = Label(win, text = j).pack()
                    else:
                        time.sleep(0.3)
                time.sleep(0.6)
                
    except KeyboardInterrupt:
        GPIO.cleanup()
    
def dot():
        led.on()
        time.sleep(0.3)
        led.off()
        time.sleep(0.3)
def dash():
        led.on()
        time.sleep(0.6)
        led.off()
        time.sleep(0.6)
    


code = {' ': '|', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
        'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
        'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
    

mbutton = Button(win, text = 'Execute', command = Mcode, fg = 'red', bg= 'blue').pack()
textEntry = Entry(win, textvariable = word).pack()
