import time
import threading

class LightSensor:
    """This is the light sensor"""

    def __init__(self,GPIO, PIN):
        self.GPIO = GPIO
        self.pin = PIN
        self.itIsLight = 0      # aflag to set if it is light
        self.gettingLight = 0   # We don't want to react to all events when the light comes on in case its someone walking by with a torch!
        self.gettingDark = 0    # We don't want to react to all events that show light has gone in case its a shadow of someone walking past.
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.pin,GPIO.BOTH,callback=self.LightLevelChanging, bouncetime=500)

    def info(self):
        print("using GPIO pin:", self.pin,"\nitIsLight is set to:",self.itIsLight)

    def LightLevelChanging(self,channel):
        time.sleep(0.1)
        print("There is a change on the pin now reads: ", self.GPIO.input(channel))
        
        if self.GPIO.input(channel):
            """ if the pin returns 1 - we think its dark"""
            self.gettingDark = 1
            t=threading.Timer(123, self.CheckLightLevelChange)
        else:
            """ if the pin returns 0 - we think its light"""
            self.gettingDark = 0
            t=threading.Timer(123, self.CheckLightLevelChange)

        self.gettingiLight = not self.gettingDark
        t.start()

    def CheckLightLevelChange(self):
        oldItIsLight = self.itIsLight
        if  self.gettingDark and self.GPIO.input(self.pin):
            self.itIsLight = 0
        elif  self.gettingiLight and not self.GPIO.input(self.pin):
            self.itIsLight = 1
        else:
            pass


        if oldItIsLight != self.itIsLight:
            print("light level changed to ", self.itIsLight)
        else:
            print("false reading - probably a bloody cat")


            

    def IsItLight():
        return self.itIsLight
        """
        now I need to raise an event or signal to let things now we have gone from light to dark
        see http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html
        or http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html
        or http://stackoverflow.com/questions/1092531/event-system-in-python
        """
