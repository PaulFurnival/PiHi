#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import argparse


parser = argparse.ArgumentParser(description='Check for movement on a PIR if no daylight is present on light sensor')
parser.add_argument('-1', dest='relay', type=int, default=22, help="GPIO Pin for Relay 1 (Default:22)")
args = parser.parse_args()


GPIO.setmode(GPIO.BCM)
GPIO.setup(args.relay,GPIO.OUT, initial=1)
time.sleep(3)

try:
    print ("looping ...")
    while 1:
        print("Turning on for 3 seconds")
        GPIO.output(args.relay,0)
        time.sleep(3)
        print("Turning off for 3 seconds")
        GPIO.output(args.relay,1)
        time.sleep(3)

except Exception as e:
    print("\n\n\nSomething went wrong!!!!\n\n\n",e,"\n\n\n")
    raise
except KeyboardInterrupt as k:
    print("exiting")
finally:
    GPIO.cleanup()
    print("I've cleaned up!")
print("\n\nCompleted!")
