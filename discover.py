from yeelight import discover_bulbs #imports the necessary functionaliy we need to find our bulb's IP Address

findIP = discover_bulbs() #creates a variable using the discover bulbs functionality

print(findIP) #prints our findings, use the IP from here to mess around with the Yeelight
