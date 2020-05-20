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

def mhello():
    mtext = word.get()
    mtext = to_morse_code(mtext)
    mlabel2 = Label(win, text = mtext).pack()
    
    for i in mtext:
        if(i == '1'):
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(1)
            
        if(i == '2'):
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(1)
            
        if(i == '3'):
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(1)
        
        if(i == '4'):
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(1)
        
        if(i == '5'):
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(1)
        
        if(i == '6'):
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(1)
            
        if(i == '7'):
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(1)
        
        if(i == '8'):
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(1)
            
        if(i == '9'):
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(1)
            
        if(i == '10'):
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(1)
            
        if(i == '11'):
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(1)
            
        if(i == '12'):
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(1)

        if(i == '13'):
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(1)
            
        if(i == '14'):
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(1)
            
        if(i == '15'):
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(1)
            
        if(i == '16'):
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(1)

        if(i == '17'):
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(1)
            
        if(i == '18'):
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(1)

        if(i == '19'):
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(1)
            
        if(i == '20'):
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(1)

        if(i == '21'):
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(1)

        if(i == '22'):
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(1)

        if(i == '23'):
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(1)

        if(i == '24'):
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(1)
            
        if(i == '25'):
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(1)

        if(i == '26'):
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(0.3)
            led.on()
            time.sleep(0.3)
            led.off()
            time.sleep(1)
        
            
        return

def to_morse_code(word):
    code = {' ': '|', 'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7',
            'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15',
            'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23',
            'x': '24', 'y': '25', 'z': '26'}
    
    morse_code = ""
    
    for x in word:
        morse_code += code[x.lower()]
    
    return morse_code

mlabel = Label(win, text = 'My Label').pack()

mbutton = Button(win, text = 'OK', command = mhello, fg = 'red', bg= 'blue').pack()

textEntry = Entry(win, textvariable = word).pack()
