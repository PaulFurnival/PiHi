from GPIODevice_class import GPIODevice

class light(GPIODevice):

    def __init__(self,name):
        GPIODevice.__init__(self,name)



    def config(self,GPIO,logger,controller,params):
        GPIODevice.config(self,GPIO,logger,controller,params)
        self.GPIO.setup(self.GPIOPin,self.GPIO.OUT, initial=1)


    def turnOn(self,requestor):
        if ('controlledby' in  self.params and self.params['controlledby'] == requestor) \
            or requestor=='MASTER':
            self.GPIO.output(self.GPIOPin,0)
            self.logger.info(self.name + " accepted turn on request form " + requestor)



    def turnOff(self,requestor):
        if ('controlledby' in  self.params and self.params['controlledby'] == requestor) \
             or requestor=='MASTER':
            self.GPIO.output(self.GPIOPin,1)
            print(self.name + " turn off called and accepted by: " + requestor)
