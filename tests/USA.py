import yeelight
from yeelight import Bulb
import time
myIP = '192.168.0.8' #sets a variable for my IP, IP will differ based on user's bulb
bulb = Bulb(myIP) #Connects to our bulb via IP

bulb.turn_on(effect="smooth") #turns on our bulb in a smooth manner

bulb.set_brightness(100)

bulb.set_rgb(255,0,0) #Sets our bulb color to Red

time.sleep(2)

bulb.set_rgb(1,1,1) #Sets our bulb color to White

time.sleep(2)

bulb.set_rgb(0,0,255)  #Sets our bulb color to Blue

print("USA")