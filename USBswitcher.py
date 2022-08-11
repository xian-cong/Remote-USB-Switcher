import streamlit as sl
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
button = 14
GPIO.setup(button, GPIO.OUT) # GPIO Assign mode

def press(): 
    sl.write('Switching...')
    GPIO.output(button, GPIO.LOW) # switch
    sleep(1)

def main():
    sl.title("USB Swithcer")
    switch = sl.button('Switch')
    while(switch):
        press()
        GPIO.output(button, GPIO.HIGH)
        switch = False
        # print(switch)

if __name__ == '__main__':
    main()
