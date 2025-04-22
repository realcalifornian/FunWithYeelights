import yeelight
from yeelight import Bulb
import time
myIP = '192.168.0.8' #sets a variable for my IP, IP will differ based on user's bulb
bulb = Bulb(myIP) #Connects to our bulb via IP

bulb.turn_on(effect="smooth") #turns on our bulb in a smooth manner

bulb.set_rgb(0,255,0) #Sets our bulb to a forgiving and soothing green

bulb.set_brightness(10) #Sets up for our clear system

for i in range(10): #
    bulb.set_brightness(100)
    print("ALL CLEAR, ALL CLEAR")

    time.sleep(1)
    bulb.set_brightness(10)

    time.sleep(1)

print("EVERYTHING IS CLEAR NOW, RETURN TO YOUR QUARTERS")