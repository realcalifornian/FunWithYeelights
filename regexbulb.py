from yeelight import Bulb
import re
import time
import random

bulb = Bulb("192.168.0.8")

identify = "Fight the light with all your might"
x = re.findall("ight", identify)

bulbpower = len(x)

for i in range(bulbpower):
    bulb.set_brightness(75)
    
    time.sleep(1)

    bulb.set_rgb(random.randint(1,30), random.randint(1,50), random.randint(1,70))

    time.sleep(1)

    bulb.set_rgb(random.randint(1,60), random.randint(1,80), random.randint(1,100))

    time.sleep(1)

    bulb.set_rgb(random.randint(1,90), random.randint(1,110), random.randint(1,130))