#!/usr/bin/env python3

import argparse
import signal
import sys
import time
import logging
from threading import Thread

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )
parser = argparse.ArgumentParser(description='Check for movement on a PIR if no daylight is present on light sensor')
parser.add_argument('-p', dest='pir', type=int, default=16, help="PIR data pin (Default: 16)")
parser.add_argument('-s', dest='sensor', type=int, default=21, help="Light Sensor data pin (Default: 21)")
parser.add_argument('-l', dest='lightOnPeriod', type=int, default=15, help="How long to put the light on when movement is detected (Default:15)")
args = parser.parse_args()

loopCount=3
itIsLight=0
sleepTime=2
sensor=args.sensor
pir=args.pir

def goneLight(o):
    global itIsLight
    print("Lighting changed to light",GPIO.input(o))
    if GPIO.input(o) == 0 and itIsLight == 0:
        logging.info("Light Level has changed to  [ ON  ]")
        itIsLight=1
        #GPIO.output(relay,GPIO.HIGH)
    else:
        logging.info("Light Level has changed to  [ OFF  ]")
        #GPIO.output(relay,GPIO.LOW)
        itIsLight=0

def weGotMovement(o):
    logging.info("Detected Movement")
    if itIsLight == 0:
        """
        We want to turn the lights on , but not forever, we want a delay in munites
        this delay is determined by the argument lightOnPeriod.
        """
        logging.info("We need some light over here!!!!")
    else:
        logging.info("No need for the lights, daylight is available")



def dummy_task():
    """
     A function that soed nothing to allow us to set up a thread 
     as a timer
     e.g. we turn the lights on when we get movement fr 10 minuts so we set a threa 
     running this empty function for 10 minutes then iot returns to the program

     see http://stackoverflow.com/questions/2831775/running-a-python-script-for-a-user-specified-amount-of-time
     """
    while true:
        pass
try:
    import RPi.GPIO as GPIO
    import time
    logging.info("using package version"+str(GPIO.VERSION))
    GPIO.setmode(GPIO.BCM)
    #GPIO.setup(relay,GPIO.OUT)                              #This is the LED
    GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(pir, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(sensor,GPIO.RISING,callback=goneLight, bouncetime=500)
    logging.info("Light sensor running on GPIO " + str(sensor))
    GPIO.add_event_detect(pir,GPIO.RISING,callback=weGotMovement, bouncetime=500)
    logging.info("PIR running on GPIO " + str(pir))
    
    #on initialisation, find out if its light or dark
    if  GPIO.input(sensor) == 1 :
        itIsLight=0
    else:
        itIsLight=1
    logging.info("on initialisation, itIsLight set to: "+str(itIsLight))


    while 1:
       #wait for an interrupt!!!
        time.sleep(1)


except Exception as e:
    print("\n\n\nSomething went wrong!!!!\n\n\n",e,"\n\n\n")
    raise
except KeyboardInterrupt as k:
    print("exiting")
finally:
    GPIO.cleanup()
    print("I've cleaned up!")

print("\n\nCompleted!")

