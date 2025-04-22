import yeelight
from yeelight import Bulb
import time
myIP = '192.168.0.8' #sets a variable for my IP, IP will differ based on user's bulb
bulb = Bulb(myIP) #Connects to our bulb via IP

bulb.turn_on(effect="smooth") #turns on our bulb in a smooth manner

bulb.set_brightness(100)

bulb.set_rgb(128,0,255) #Sets our bulb color to Purple

time.sleep(2)

bulb.set_rgb(128,128,128) #Sets our bulb color to Grey

print("Go Rockies! They may get 50 wins!")