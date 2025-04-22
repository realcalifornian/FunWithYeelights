import yeelight
from yeelight import Bulb
import time
myIP = '192.168.0.8' #sets a variable for my IP
bulb = Bulb(myIP) #Connects to our bulb via IP

bulb.turn_on(effect="smooth") #turns on our bulb in a smooth manner

bulb.set_brightness(100)

bulb.set_rgb(128,0,32) #Sets our bulb color to Burgundy

time.sleep(2)

bulb.set_rgb(0,0,255) #Sets our bulb color to Blue

print("Go Avs!")