class GPIODevice:

    def __init__(self,name):
        self.name = name


    def config(self,GPIO,logger,controller,params):
        self.description=params['description']
        self.GPIO = GPIO
        self.GPIOPin = int(params['GPIOPin'])
        self.params = params
        self.logger=logger
        self.controller = controller    # a reference back to the controller object


    def info(self):
        for key in self.params:
            print(self.params[key])


    def start(self):
        pass


    def status(self):
        print(self.description)
