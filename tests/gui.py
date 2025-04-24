from flask import Flask, render_template, request  
app = Flask(__name__) # Flask constructor
import os
from yeelight import Bulb
from Nuggets import Nuggets
from Avs import Avs
from Broncos import Broncos
from ColorCycle import ColorWheel
from LeBulb import Lakers
from RedAlert import RedAlert
from Rockies import Rockies
from Safety import Safety
from USA import USA
  

myIP = '192.168.0.8'
bulb = Bulb(myIP)

picFolder = os.path.join('static','pics') #allows us to access our folder holding every necessary image for later

app.config['UPLOAD_FOLDER'] = picFolder #gives us access to our upload folder as well, allowing image uploads

# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def introduction(): 
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'Colorwheelyeelight.JPG') #gives our first picture a variable
    try:
        test = request.args["Button1"]
        print(test)
    except:
        pass
    return render_template(
        "index.html",
        demoimage = pic1, #turns our variable into another that's used in the index.html file
        titletext = "Welcome to the Yeelight Fun Operation"
        
    )
  

@app.route('/customs')
def custom_route():
    redalert = os.path.join(app.config['UPLOAD_FOLDER'], 'RedAlertyeelight.JPG')
    safety = os.path.join(app.config['UPLOAD_FOLDER'], 'Safetyyeelight.JPG')
    USApic = os.path.join(app.config['UPLOAD_FOLDER'], 'USAyeelight.JPG')
    colorwheel = os.path.join(app.config['UPLOAD_FOLDER'], 'Colorwheelyeelight.JPG')
    try:
        special = request.args["Button3"]
        print(special)
        if special == "RedAlert":
            RedAlert(myIP).start()
        elif special == "Safety":
            Safety(myIP).start()
        elif special == "USA":
            USA(myIP).start()
        elif special == "ColorWheel":
            ColorWheel(myIP).start()
        else:
            bulb.set_rgb(1,1,1)
    except:
        pass
    return render_template(
        "customs.html",
        customtext = "Below are some random custom light patterns",
        demored = redalert,
        demogreen = safety,
        demoUSA = USApic,
        demowheel = colorwheel
    )

@app.route('/sports')
def sport_route():
    broncos = os.path.join(app.config['UPLOAD_FOLDER'], 'Broncosyeelight.JPG')
    avs = os.path.join(app.config['UPLOAD_FOLDER'], 'Avsyeelight.JPG')
    nuggets = os.path.join(app.config['UPLOAD_FOLDER'], 'Nuggetsyeelight.JPG')
    rockies = os.path.join(app.config['UPLOAD_FOLDER'], 'Rockiesyeelight.JPG')
    lakers = os.path.join(app.config['UPLOAD_FOLDER'], 'Lakersyeelight.JPG')
    try:
        team = request.args["Button2"]
        print(team)
        if team == "Broncos":
            Broncos(myIP).start()
        elif team == "Avs":
            Avs(myIP).start()
        elif team == 'Nuggets':
            Nuggets(myIP).start()
        elif team == 'Rockies':
            Rockies(myIP).start()
        elif team == 'Lakers':
            Lakers(myIP).start()
        else:
            bulb.set_rgb(1,1,1)
    except:
        pass
    return render_template(
        "sports.html",
        sportstext = "Below are some random custom light patterns specifically for sports teams",
        demobroncos = broncos,
        demoavs = avs,
        demonuggets = nuggets,
        demorockies = rockies,
        demolakers = lakers
    )


if __name__=='__main__': 
   app.run(host="127.0.0.1", port=8080)