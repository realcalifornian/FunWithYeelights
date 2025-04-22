from flask import Flask, render_template, request  
app = Flask(__name__) # Flask constructor 
import os   
  
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
    USA = os.path.join(app.config['UPLOAD_FOLDER'], 'USAyeelight.JPG')
    colorwheel = os.path.join(app.config['UPLOAD_FOLDER'], 'Colorwheelyeelight.JPG')
    return render_template(
        "customs.html",
        customtext = "Below are some random custom light patterns",
        demored = redalert,
        demogreen = safety,
        demoUSA = USA,
        demowheel = colorwheel
    )

@app.route('/sports')
def sport_route():
    broncos = os.path.join(app.config['UPLOAD_FOLDER'], 'Broncosyeelight.JPG')
    avs = os.path.join(app.config['UPLOAD_FOLDER'], 'Avsyeelight.JPG')
    nuggets = os.path.join(app.config['UPLOAD_FOLDER'], 'Nuggetsyeelight.JPG')
    rockies = os.path.join(app.config['UPLOAD_FOLDER'], 'Rockiesyeelight.JPG')
    lakers = os.path.join(app.config['UPLOAD_FOLDER'], 'Lakersyeelight.JPG')
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