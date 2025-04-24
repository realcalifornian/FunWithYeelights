import yeelight
from yeelight import Bulb
import time
from yeelightclass import YeeLightClass

class Safety(YeeLightClass):
    def __init__(self, myIP):
        super().__init__(myIP)

    def start(self):
        self.bulb.turn_on(effect="smooth") #turns on our bulb in a smooth manner

        self.bulb.set_rgb(0,255,0) #Sets our bulb to a forgiving and soothing green

        self.bulb.set_brightness(10)
        for i in range(10): #
            self.bulb.set_brightness(100)
            print("ALL CLEAR, ALL CLEAR")

            time.sleep(1)
            self.bulb.set_brightness(10)

            time.sleep(1)

        print("EVERYTHING IS CLEAR NOW, RETURN TO YOUR QUARTERS")

if __name__ == "__main__":
    Safety(myIP='192.168.0.8').start()