#!/usr/bin/env python3

import argparse
import signal
import sys
import time
import logging
from PiHiController_class import PiHiController
from threading import Thread
import datetime
import RPi.GPIO as GPIO
from ls_class import LightSensor
import configparser

config = configparser.ConfigParser()
config.read('PiHi.ini')
print(config.sections())
for key in config['DEVICES']: 
    print(key)
#    for key2 in config[key]: 
#        print("key2 is:2 ",key2)
#        print(config[key2])




GPIO.setmode(GPIO.BCM)


parser = argparse.ArgumentParser(description='Check for movement on a PIR if no daylight is present on light sensor')
args = parser.parse_args()

fname = "/var/log/PiHi/PiHilog_" + datetime.datetime.today().strftime("%Y-%m-%d_%H-%M-%S")+ ".log"
logging.basicConfig(filename=fname, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

PHC = PiHiController(args)
PHC.check()


ls = LightSensor(GPIO,21)


try:
    while 1:
        pass

except Exception as e:
    print("\n\n\nSomething went wrong!!!!\n\n\n",e,"\n\n\n")
    raise
except KeyboardInterrupt as k:
    print("exiting")
finally:
    GPIO.cleanup()
    print("I've cleaned up!")

print("\n\nCompleted!")
