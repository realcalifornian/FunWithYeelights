import yeelight
from yeelight import Bulb
import time
from yeelightclass import YeeLightClass

class USA(YeeLightClass):
    """
    Using the Abstract YeelightClass, this code is used for creating a patriotic USA flash chant that utilizes the Yeelight's colorshifting functionality
    """
    def __init__(self, myIP):
        super().__init__(myIP)

    def start(self):
        self.bulb.turn_on(effect="smooth") #turns on our bulb in a smooth manner

        self.bulb.set_brightness(100)
        for i in range(3):
            self.bulb.set_rgb(255,0,0) #Sets our bulb color to Red

            time.sleep(1)

            self.bulb.set_rgb(1,1,1) #Sets our bulb color to White

            time.sleep(1)

            self.bulb.set_rgb(0,0,255)  #Sets our bulb color to Blue

            time.sleep(1)
            
            print("USA")


if __name__ == "__main__":
    USA(myIP='192.168.0.8').start()