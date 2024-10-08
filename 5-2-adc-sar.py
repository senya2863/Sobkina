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

def adc():
    value=0
    for i in range (7,-1,-1):
        value+=2**i
        signal=binar(value)
        GPIO.output(dac,signal)
        time.sleep(0.001)
        comparv=GPIO.input(14)
        if comparv>0:
            value-=2**i
    return value

try:
    while True:
        value=adc()
        voltage=value/256*3.3
        print(value, voltage)

finally:
    GPIO.output(dac,0)
    GPIO.output(troyka,0)
    GPIO.cleanup()