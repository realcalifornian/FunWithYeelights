import yeelight
from yeelight import Bulb
class YeeLightClass:
    """
    Abstract Class
    """
    def __init__(self, myIP):
        
        self.myIP = myIP #sets a variable for my IP that can be altered within individual scripts
        self.bulb = Bulb(self.myIP) #Connects to our bulb via IP
    def start(self): #this section of the class will be altered based on which lightbulb commands are used in other scripts
        pass