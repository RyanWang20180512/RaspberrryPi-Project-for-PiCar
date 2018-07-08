import RPi.GPIO as GPIO
import time
import sys

class Motor(object):
    '''Motor control'''
    def __init__(self,ENA,IN1,IN2,IN3,IN4,ENB):
        '''Specify motor pins'''
        self.enab_pin=[ENA,ENB] #Enable pins
        self.inx_pin=[IN1,IN2,IN3,IN4] #Control pins
        
        self.RightAhead_pin=self.inx_pin[3]
        self.RightBack_pin=self.inx_pin[2]
        self.LeftAhead_pin=self.inx_pin[1]
        self.LeftBack_pin=self.inx_pin[0]

        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for pin in self.inx_pin:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin,GPIO.LOW)

        pin=None

        for pin in self.enab_pin:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin,GPIO.HIGH)

    def ahead(self):
        for pin in self.inx_pin:
            GPIO.output(pin,GPIO.LOW)

        GPIO.output(self.RightAhead_pin,GPIO.HIGH)
        GPIO.output(self.LeftAhead_pin,GPIO.HIGH)

    def left(self):
        for pin in self.inx_pin:
            GPIO.output(pin,GPIO.LOW)
        GPIO.output(self.RightAhead_pin,GPIO.HIGH)
        GPIO.output(self.LeftBack_pin,GPIO.HIGH)

    def right(self):
        for pin in self.inx_pin:
            GPIO.output(pin,GPIO.LOW)
        GPIO.output(self.LeftAhead_pin,GPIO.HIGH)
        GPIO.output(self.RightBack_pin,GPIO.HIGH)

    def rear(self):
        for pin in self.inx_pin:
            GPIO.output(pin,GPIO.LOW)
        GPIO.output(self.RightBack_pin,GPIO.HIGH)
        GPIO.output(self.LeftBack_pin,GPIO.HIGH)

    def stop(self):
        for pin in self.inx_pin:
            GPIO.output(pin,GPIO.LOW)

    def clear(self):
        GPIO.cleanup()
