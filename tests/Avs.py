import yeelight
from yeelight import Bulb
import time
from yeelightclass import YeeLightClass

class Avs(YeeLightClass):
    """
    Using the Abstract YeelightClass, this code is used for creating the Avs version of the Yeelight colorshifting functionality
    """
    def __init__(self, myIP):
        super().__init__(myIP)

    def start(self):
        self.bulb.turn_on(effect="smooth") #turns on our bulb in a smooth manner

        self.bulb.set_brightness(100)

        self.bulb.set_rgb(128,0,32) #Sets our bulb color to Burgundy Red

        time.sleep(2)

        self.bulb.set_rgb(0,0,255) #Sets our bulb color to Dark Blue

        print("Go Avs, FUTURE 2025 STANLEY CUP CHAMPIONS!")

if __name__ == "__main__":
    Avs(myIP='192.168.0.8').start() #starts our program