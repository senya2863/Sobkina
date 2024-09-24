import RPi.GPIO as GPIO
import sys
from time import sleep
dac=[8,11,7,1,8,5,12,6] 
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
def binary (a,n):
    return [int(elem) for elem in bin(a) [2:].zfill(n)]
try:
    while True :
        print ("0-255")
        num=input()
        if num=="q":
            sys.exit()
        elif num.isdigit() and int(num)%1==0 and 0<=int(num)<=255:
            GPIO.output(dac,binary(int(num),8))
            sleep(10)
            print ("{:.4f}".format(int(num)/256*3.3))
        elif not(num.isdigit()):
            print("num is not digit")
except ValueError:
    print ("input num 0-255")
except KeyboardInterrupt:
    print ("done")
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()