#!/usr/bin/python37all
# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output
import RPi.GPIO as GPIO
import time
import json


green = 19
yellow = 13
red = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)


#json
with open('lab4.txt'
, 'r') as f:
  data = json.load(f)
print("button = " + str(data['option']))
print("slider 1 = " + str(data['slider1']))


#start with leds off
pwm1 = GPIO.PWM(green, 100) # PWM object on our pin at 100 Hz
pwm1.start(0) # start with LED off
pwm2 = GPIO.PWM(yellow, 100) # PWM object on our pin at 100 Hz
pwm2.start(0) # start with LED off
pwm3 = GPIO.PWM(red, 100) # PWM object on our pin at 100 Hz
pwm3.start(0) # start with LED off

while True:
  with open("lab4.txt", 'r') as f:
    dutyCycle = float(f.read()) # read duty cycle value from file
  if ('option' == 1):
    pwm1.ChangeDutyCycle(dutyCycle)
    time.sleep(0.1)
  elif ('option' == 2):
    pwm2.ChangeDutyCycle(dutyCycle)
    time.sleep(0.1)
  elif ('option' == 3):
    pwm3.ChangeDutyCycle(dutyCycle)
    time.sleep(0.1)


