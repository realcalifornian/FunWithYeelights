import yeelight
from yeelight import Bulb
import time
myIP = '192.168.0.8' #sets a variable for my IP, IP will differ based on user's bulb
bulb = Bulb(myIP) #Connects to our bulb via IP

bulb.set_rgb(10,15,20)

time.sleep(2)

rgbX = 100

rgbY = 40

rgbZ = 105

for i in range(15):
    bulb.set_rgb(rgbX,rgbY,rgbZ)
    i = i + 1
    rgbX = (rgbX - 15)
    rgbY = (rgbY + (i + 2))
    rgbZ = (rgbZ * (i + 2))

    time.sleep(2)

print("Enjoy the Fun?")