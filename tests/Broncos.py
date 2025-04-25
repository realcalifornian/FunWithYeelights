import yeelight
from yeelight import Bulb
import time
from yeelightclass import YeeLightClass

class Broncos(YeeLightClass):
    """
    Using the Abstract YeelightClass, this code is used for creating the Broncos version of the Yeelight colorshifting functionality
    """
    def __init__(self, myIP):
        super().__init__(myIP)

    def start(self):
        self.bulb.turn_on(effect="smooth") #turns on our bulb in a smooth manner

        self.bulb.set_brightness(100)

        self.bulb.set_rgb(255,140,0) #Sets our bulb color to Orange

        time.sleep(2)

        self.bulb.set_rgb(0,0,255) #Sets our bulb color to Blue

        print("Go Broncos, Bo Nix is my savior!")

if __name__ == "__main__":
    Broncos(myIP='192.168.0.8').start()