import yeelight
from yeelight import Bulb
import time
from yeelightclass import YeeLightClass

class Nuggets(YeeLightClass):
    def __init__(self, myIP):
        super().__init__(myIP)

    def start(self):
        self.bulb.turn_on(effect="smooth") #turns on our bulb in a smooth manner

        self.bulb.set_brightness(100)

        self.bulb.set_rgb(255,255,0) #Sets our bulb color to Yellow

        time.sleep(2)

        self.bulb.set_rgb(0,0,120) #Sets our bulb color to Dark Blue

        print("Go Nuggets! I love you Nikola Jokic!")

if __name__ == "__main__":
    Nuggets(myIP='192.168.0.8').start() #starts the program

