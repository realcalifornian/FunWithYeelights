import yeelight
from yeelight import Bulb
import time
from yeelightclass import YeeLightClass

class Lakers(YeeLightClass):
    def __init__(self, myIP):
        super().__init__(myIP)

    def start(self):
        self.bulb.turn_on(effect="smooth") #turns on our bulb in a smooth manner

        self.bulb.set_brightness(100)

        self.bulb.set_rgb(128,0,255) #Sets our bulb color to Purple

        time.sleep(2)

        self.bulb.set_rgb(255,255,0) #Sets our bulb color to Yellow

        print("LeBron is the GOAT!!")


if __name__ == "__main__":
    Lakers(myIP='192.168.0.8').start() #starts our script