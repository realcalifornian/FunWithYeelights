import yeelight
from yeelight import Bulb
import time
from yeelightclass import YeeLightClass

class Rockies(YeeLightClass):
    """
    Using the Abstract YeelightClass, this code is used for creating the Rockies version of the Yeelight colorshifting functionality
    """
    def __init__(self, myIP):
        super().__init__(myIP)

    def start(self):
        self.bulb.turn_on(effect="smooth") #turns on our bulb in a smooth manner

        self.bulb.set_brightness(100)

        self.bulb.set_rgb(128,0,255) #Sets our bulb color to Purple

        time.sleep(2)

        self.bulb.set_rgb(128,128,128) #Sets our bulb color to Grey

        print("Go Rockies! They may get 50 wins!")


if __name__ == "__main__":
    Rockies(myIP='192.168.0.8').start()