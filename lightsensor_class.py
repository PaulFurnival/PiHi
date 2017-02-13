
import signal
import sys
import time
import logging
from threading import Thread
from GPIODevice_class import GPIODevice


class lightSensor(GPIODevice):
    def __init__(self, name):
        GPIODevice.__init__(self,name)

    def config(self, GPIO, logger,controller,params):
        GPIODevice.config(self, GPIO, logger, controller,params)
        print(self.name,"->",self.GPIOPin)


    def start(self):
        self.GPIO.setup(self.GPIOPin, self.GPIO.IN, pull_up_down=self.GPIO.PUD_DOWN)
        self.GPIO.add_event_detect(self.GPIOPin,self.GPIO.BOTH,callback=self.goneLight, bouncetime=500)
    
        #on initialisation, find out if its light or dark
        if  self.GPIO.input(self.GPIOPin) == 1 :
            self.itIsLight=0
        else:
            self.itIsLight=1
        self.logger.info("on initialisation, itIsLight set to: "+str(self.itIsLight))
        

    def goneLight(self,o):
#        global itIsLight
        time.sleep(.4)   # lets give the GPIO pin time to settle!!!!
        if self.GPIO.input(o) == 0 and self.itIsLight == 0:
            self.logger.info(self.name + " Reports Light Level has changed to  [ ON  ]")
            self.itIsLight=1
        else:
            self.logger.info(self.name + "Reports that Light Level has changed to  [ OFF  ]")
            self.itIsLight=0
        self.controller.gonelight(self.itIsLight)

    def isItLight(self):
        return self.itIsLight

    def status(self):
        if self.itIsLight:
            status="Light"
        else:
            status="Dark"
        print("Light sensor thinks it is: ",status)
            

"""
def dummy_task():
    " " "
     A function that soed nothing to allow us to set up a thread 
     as a timer
     e.g. we turn the lights on when we get movement fr 10 minuts so we set a threa 
     running this empty function for 10 minutes then iot returns to the program

     see http://stackoverflow.com/questions/2831775/running-a-python-script-for-a-user-specified-amount-of-time
     " " "
    while true:
        pass
try:
    import time
    logging.info("using package version"+str(GPIO.VERSION))
    GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
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
"""
