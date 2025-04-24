import yeelight
from yeelight import Bulb
import time
from yeelightclass import YeeLightClass
import random

class ColorWheel(YeeLightClass):
    def __init__(self, myIP):
        super().__init__(myIP)

    def start(self):
        self.bulb.turn_on(effect="smooth") #turns on our bulb in a smooth manner

        self.bulb.set_rgb(1,1,1)

        self.bulb.set_brightness(75)

        time.sleep(2)

        rgbX = random.randint(1,100)

        rgbY = random.randint(1,120)

        rgbZ = random.randint(1,110)
        for i in range(15):
            self.bulb.set_rgb(rgbX,rgbY,rgbZ) #uses our variables above to set an initial random color to the bulb
            i = i #hastens our script and changes our i values for the sake of altering the bulb's color even further
            rgbX = (rgbX - 5)
            rgbY = (rgbY + (i + random.randint(5,20)))
            rgbZ = (rgbZ * (i + random.randint(2,40)))

            time.sleep(1)
        print("Enjoy the fun?")

if __name__ == "__main__":
    ColorWheel(myIP='192.168.0.8').start()