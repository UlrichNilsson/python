#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11
PushPin = 10

def setup():
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(PushPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def loop():
    while True:
        print('...led on')
        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(0.5)
        print('led off...')
        GPIO.output(LedPin, GPIO.HIGH) # led off
        time.sleep(0.5)
        while GPIO.input(10) == GPIO.HIGH:
            GPIO.output(LedPin,GPIO.HIGH)
            #print('Press')

def destroy():
    GPIO.output(LedPin, GPIO.HIGH)     # led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
            loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
            destroy()
