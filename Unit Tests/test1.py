import yeelight
from yeelight import Bulb
import time

bulb = Bulb('192.168.0.8') #sets our bulb's IP, as found with discover.py. Use your own special one discovered rather than mine

bulb.turn_off() #turns off the lightbulb

time.sleep(3) #waits 3 seconds

bulb.turn_on() #turns on the lightbulb

bulb.set_brightness(10) #dims the lightbulb's brightness to 10

time.sleep(3) #waits 3 seconds

bulb.set_brightness(100) #Completely brightens the lightbulb