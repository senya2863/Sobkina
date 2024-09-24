import RPi.GPIO as GPIO
from time import sleep

dac=[8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)

def perev(a):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]

try:
    t = input()

    if not t.isdigit():
        print("is not digit")
        exit

    tim = int(t)

    while True:
        for i in range (255):
            print(i)
            num = perev(i)
            print(num)
            GPIO.output(dac, num)
            sleep(tim / 512)

        for i in range (255,0,-1):
            GPIO.output(dac, perev(i))
            sleep(tim / 512)

finally:
    GPIO.output(dac,0)
    GPIO.cleanup()