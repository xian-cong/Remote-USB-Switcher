import streamlit as sl
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
button = 17
GPIO.setup(button, GPIO.OUT) # GPIO Assign mode


def main():
    sl.title("USB Swithcer")
    switch = sl.button('Switch')
    if switch:
        sl.write('Switching...')
        GPIO.output(button, GPIO.HIGH) # on
        