import yeelight
from yeelight import Bulb
import time
from yeelightclass import YeeLightClass

class RedAlert(YeeLightClass):
    """
    Using the Abstract YeelightClass, this code is used for creating an alarming red blinking lightbulb utilizing the Yeelight's colorshift and brightness shift functionalities
    """
    def __init__(self, myIP):
        super().__init__(myIP)

    def start(self):
        self.bulb.turn_on(effect="smooth") #turns on our bulb in a smooth manner

        self.bulb.set_rgb(255,0,0) #Sets our bulb to an intense red color

        self.bulb.set_brightness(10) #Sets up for our alert system

        for i in range(10): #
            self.bulb.set_brightness(100)
            
            print("RED ALERT, RED ALERT")

            time.sleep(1)
            self.bulb.set_brightness(10)

            time.sleep(1)

        print("WARNING HAS ENDED, WARNING HAS ENDED")


if __name__ == "__main__":
    RedAlert(myIP='192.168.0.8').start() #starts the program