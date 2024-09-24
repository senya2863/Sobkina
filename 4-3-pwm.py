import RPi.GPIO as GPIO
import sys
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
dac=[8,11,7,1,0,5,12,6] 
GPIO.setup(dac,GPIO.OUT,initial=GPIO.HIGH)
pwm=GPIO.PWM(2,1000)
pwm.start(0)
try:
    while True:
        DC=int(input())
        pwm.ChangeDutyCycle(DC)
        print("{:.2f}".format(DC*3.3/100))
finally:
    GPIO.output(2,0)
    GPIO.output(dac,0)
    GPIO.cleanup()