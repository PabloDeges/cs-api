#!usr/local/bin/python3

from flask import Flask, url_for, render_template
from flask_restful import Resource, Api
import json
import random

app = Flask(__name__)
api = Api(app)

data = {}
class_data = {}
weapon_data = {}

with open("cs_data.json", "r") as f:
    data = json.load(f)
with open("cs_class_data.json", "r") as f:
    class_data = json.load(f)
with open("cs_weapon_data.json", "r") as f:
    weapon_data = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/info")
def info():
    return render_template("api.html")
@app.route("/loadout")
def loadout():
    glock = random.choice(weapon_data["Glock-18"])
    usp = random.choice(weapon_data["USP-S"])
    deagle = random.choice(weapon_data["Desert Eagle"])
    ak47 = random.choice(weapon_data["AK-47"])
    m4a1 = random.choice(weapon_data["M4A1-S"])
    awp= random.choice(weapon_data["AWP"])
    ump =random.choice(weapon_data["UMP-45"])
    scout =random.choice(weapon_data["SSG 08"])
    knife =random.choice(weapon_data["Knife"])
    gloves =random.choice(weapon_data["Gloves"])
    price_sum = float(usp["price"]) + float(glock["price"]) + float(deagle["price"]) +float(ak47["price"]) +float(m4a1["price"])+float(awp["price"])+float(ump["price"])+float(scout["price"])+float(knife["price"])+float(gloves["price"])
    copy_text = knife["name"]+  " " + gloves["name"] +  " "+ glock["name"] +  " "+ usp["name"] +  " "+ deagle["name"] +  " "+ ak47["name"] +  " "+ m4a1["name"] +  " "+ awp["name"] +  " "+ ump["name"] +  " "+ scout["name"]
    formatted_sum = "{:.2f}".format(price_sum)
    return render_template("loadout.html", glock=glock, usp=usp, deagle=deagle, ak47 = ak47, m4a1 = m4a1, awp=awp, ump=ump, scout=scout, formatted_sum=formatted_sum, knife=knife, gloves=gloves, copy_text=copy_text)

## API


    




class Specific_Skin(Resource):

    def get(self, skin_name):
        return data[skin_name]
    
class Random_Skin(Resource):
    def get(self):
        res = random.sample(data.items(), 1)
        return res
    
class Random_Skin_From_Class(Resource):
    def get(self, class_name):
        list = class_data[class_name]
        return random.choice(list)
    
class Random_Skin_From_Weapon(Resource):
    def get(self, weapon_name):
        list = weapon_data[weapon_name]
        return random.choice(list)
        
    
api.add_resource(Specific_Skin, "/api/<skin_name>")
api.add_resource(Random_Skin, "/api/random")
api.add_resource(Random_Skin_From_Class, "/api/randomclass/<class_name>")
api.add_resource(Random_Skin_From_Weapon, "/api/random/<weapon_name>")

if __name__ == "__main__":
    app.run("0.0.0.0", port=8000, debug=True)

