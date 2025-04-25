# Introduction

Welcome to the **FunWithYeelights** package!

In this package, you'll find simple codes used effectively to mess with Yeelight bulbs in a multitude of ways

As a quick disclaimer, you must have a Yeelight at home in order for this package to serve a purpose AND make sure to change the IP address based on your specific Yeelight, as mine won't be the exact same as yours for obvious reasons.

Have fun!

# Startup

Begin with using the discover.py program to find Yeelight bulbs connected to your local network OR use the **Yeelight Classic** app and go to Device -> (device_name) -> Settings -> Device Info to find the bulb's IP Address there.

Additionally, you can statically assign your Yeelight an IP so that it falls in line with my scripts right off the bat. To do so, you must edit it through your router's administration, please research for more information regarding specifics like that!

Either way, you can begin having fun once you've found your IP and implemented it within any of the scripts that utilize it, which is definitely easiest in gui.py since it incorporates all other special functions while only needing the user to implement their IP once.