#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import picamera

camera = picamera.PiCamera()

LedPin = 11    # pin 11
PushPin = 10    # pin 10

def setup():
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(PushPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(LedPin, GPIO.LOW) # Set LedPin high(+3.3V) to off led

def loop():
    while True:
    
        #GPIO.output(LedPin, GPIO.LOW)  # led on
        #time.sleep(0.5)
        print('No one are ringing door bell')
        GPIO.output(LedPin, GPIO.LOW) # led off
        time.sleep(0.5)
        while GPIO.input(10) == GPIO.HIGH:
            GPIO.output(LedPin,GPIO.HIGH)
            print('Door bell are ringing')
            time.sleep(0.5)
            camera.start_preview()
            camera.capture('DoorBell.jpg')
            camera.stop_preview()
def destroy():
    GPIO.output(LedPin, GPIO.HIGH)     # led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
            loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
            destroy()
