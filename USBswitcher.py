import streamlit as sl
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
button = 14
GPIO.setup(button, GPIO.OUT) # GPIO Assign mode

def press(): 
    GPIO.output(button, GPIO.HIGH)
    if switch:
        sl.write('Switching...')
        GPIO.output(button, GPIO.LOW) # switch
        press()

def main():
    sl.title("USB Swithcer")
    switch = sl.button('Switch')
    press()
    

if __name__ == '__main__':
    main()
        