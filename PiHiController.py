class PiHiController:
    """
    The main controller class
    The calling script is reponsible for setting the default values, 
    preferably by using the args class
    """

    def __init__(self,args):
        self.args = args

    def check(self):
        print(self.args)
