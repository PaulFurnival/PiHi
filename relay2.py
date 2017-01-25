#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time




GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT, initial=1)
GPIO.setup(23,GPIO.OUT, initial=1)
GPIO.setup(24,GPIO.OUT, initial=1)
GPIO.setup(25,GPIO.OUT, initial=1)

try:
    print ("looping ...")
    for x in range(4):
        GPIO.output((22+x),0)
        time.sleep(3)
        GPIO.output((22+x),1)

except Exception as e:
    print("\n\n\nSomething went wrong!!!!\n\n\n",e,"\n\n\n")
    raise
except KeyboardInterrupt as k:
    print("exiting")
finally:
    GPIO.cleanup()
    print("I've cleaned up!")
print("\n\nCompleted!")
