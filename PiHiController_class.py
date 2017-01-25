import argparse
import configparser
from threading import Thread
import datetime
import RPi.GPIO as GPIO
from ls_class import LightSensor

class PiHiController:
    """
    The main controller class
    The calling script is reponsible for setting the default values, 
    preferably by using the args class
    """

    def __init__(self,args):
        self.args = args
        self.config = configparser.ConfigParser()
        self.config.read('PiHi.ini')
        print(self.config.sections())
        for key in config['DEVICES']: 
            print(key)
        #    for key2 in config[key]: 
        #        print("key2 is:2 ",key2)
        #        print(config[key2])
#ls = LightSensor(GPIO,21)



        parser = argparse.ArgumentParser(description='Check for movement on a PIR if no daylight is present on light sensor')
        args = parser.parse_args()

    def check(self):
        print(self.args)



