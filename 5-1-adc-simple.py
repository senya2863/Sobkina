import RPi.GPIO as GPIO
import time

dac=[8,11,7,1,0,5,12,6]
compar=14
troyka=13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(compar,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(compar,GPIO.IN)
#GPIO.output(troyka,0)

def binar(a):
    return [int(i) for i in bin(a)[2:].zfill(8)]

def num2dac(value):
    signal=binar(value)
    GPIO.output(dac,signal)
    return signal

try:
    while True:
        for i in range (256):
            sign=num2dac(i)
            voltage = i*3.3/256
            time.sleep(0.01)

            compv=GPIO.input(compar)
            if compv>0:
                print('{:.2f}'.format(i,sign,voltage))
                break

finally:
    GPIO.output(dac,GPIO.LOW)
    GPIO.output(troyka,0)
    GPIO.cleanup(dac)
