from GPIODevice_class import GPIODevice

class pir(GPIODevice):

    def __init__(self,name):
        GPIODevice.__init__(self,name)



    def config(self,GPIO,logger,controller,params):
        GPIODevice.config(self,GPIO,logger,controller,params)



    def start(self):
       self.GPIO.setup(self.GPIOPin, self.GPIO.IN, pull_up_down=self.GPIO.PUD_DOWN)
       self.GPIO.add_event_detect(self.GPIOPin,self.GPIO.BOTH,callback=self.weGotMovement, bouncetime=500)
       self.lastMovementTime = 0
       print("lastmovement time is: " + str(self.lastMovementTime ))


    def weGotMovement(self,o):
        import time
        """
        we dont want to continually report movement so we'll take a note of the time,
        if its not alt least 1 minute since the last movmemnt, we'll assume this is the same person
        walking about!!!
        """
        now = time.time()
        if now - self.lastMovementTime > 60:
            self.logger.info(self.name + " Detected movement at: " + str(now))
            self.lastMovementTime = now
            self.controller.movementDetected(self.name,o)
        else:
            self.logger.info(self.name + " Detected repeat movement and did not report it to the controller at: " + str(now))
            

    def resetTimer(self):
        self.lastMovementTime = 0
