# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time

class Rotation:
        '''This class represent a SG90 module'''
	frequency=50 #Impulse frequency(Hz)
	delta_theta=0.2 #Rotation interval(degree)
	min_delay=0.0006 #The theoretical time to rotate delta_theta(s)
	max_delay=0.4 #The time to rotate from 0 to 180(s)
	
	def __init__(self,channel,min_theta,max_theta,init_theta=0):
		self.channel=channel #Control pin
		if(min_theta<0 or min_theta>180):
			self.min_theta=0
		else:
			self.min_theta=min_theta
		if(max_theta<0 or max_theta>180):
			self.max_theta=180
		else:
			self.max_theta=max_theta
                if(init_theta<min_theta or init_theta>max_theta):
                    self.init_theta=(self.min_theta+self.max_theta)/2
                else:
		    self.init_theta=init_theta #Initial theta
                self.min_dutycycle=2.5+self.min_theta*10/180
                self.max_dutycycle=2.5+self.max_theta*10/180
		
		
	def setup(self):
		'''
		Init
		'''
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.channel,GPIO.OUT)
		self.pwm=GPIO.PWM(self.channel,Rotation.frequency) #PWM
		self.dutycycle=2.5+self.init_theta*10/180 #The initial dutycycle
		self.pwm.start(self.dutycycle)
		time.sleep(Rotation.max_delay)
	
	def positiveRotation(self):
		'''
		Positive rotation，rotating delta_theta each invoking
		'''
		self.dutycycle=self.dutycycle+Rotation.delta_theta*10/180
		if self.dutycycle>self.max_dutycycle:
			self.dutycycle=self.max_dutycycle
		self.pwm.ChangeDutyCycle(self.dutycycle)
		time.sleep(Rotation.min_delay)
		
	def reverseRotation(self):
		'''
		Reverse rotation，rotating delta_theta each invoking
		'''
		self.dutycycle=self.dutycycle-Rotation.delta_theta*10/180
		if self.dutycycle<self.min_dutycycle:
			self.dutycycle=self.min_dutycycle
		self.pwm.ChangeDutyCycle(self.dutycycle)
		time.sleep(Rotation.min_delay)
		
	def specifyRotation(self,theta): 
		'''
		Rotate to specify theta
		'''
                if(theta<0 or theta>180):
			return
		self.dutycycle=2.5+theta*10/180
		self.pwm.ChangeDutyCycle(self.dutycycle)
		time.sleep(Rotation.max_delay)
		
	def cleanup(self):
		self.pwm.stop()
		time.sleep(Rotation.min_delay)
		GPIO.cleanup()
