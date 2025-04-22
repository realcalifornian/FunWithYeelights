import yeelight
from yeelight import Bulb
import time

bulb = Bulb('192.168.0.8') #sets our bulb's IP, as found with discover.py. Use your own special one discovered rather than mine

bulb.set_rgb(255,0,0) #sets our bulb to red

time.sleep(1) #hesitates for 1 sec

bulb.set_rgb(0,255,0) #sets our bulb to green

time.sleep(1) #hesitates for 1 sec

bulb.set_rgb(0,0,255) #sets our bulb to blue