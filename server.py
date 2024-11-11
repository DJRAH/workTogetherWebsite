from flask import Flask
from flask import render_template
import requests
import sqlalchemy as db


list_cafes = []

app = Flask(__name__)

#initilase db connection
engine = db.create_engine('sqlite:///cafes.db')
conn = engine.connect()
metadata = db.MetaData()
t_cafe = db.Table('cafe', metadata, autoload_with=engine)


if __name__  == "__name__":
    app.run(debug =True) 



@app.route("/")
def home():
  
    #select all cafes from db
    query = t_cafe.select()
    exe = conn.execute(query)
    all_cafes = exe.all()
    

    #put all latitude, longitude of cafes on a marker    
    markers="markers=color:red%7Clabel:S"         

    #get long and lat of cafe from url_map for show on google map
    for ca in all_cafes:
        response = requests.get(ca[2])  #get cafe_url
        adr = response.request.path_url
        cord = adr.split('z/')
        if cord != None:
            corde = cord[0]
            co = corde.split('/%40')
            if len(co) > 1 :
                markers+="%7C"
                col = co[1]
                cordinates = col.split(',')
                markers+=(cordinates[0]+','+cordinates[1])
           

    #variables needed and used on index.html            
    nbre_lignes = int(len(all_cafes)/3)+(len(all_cafes)%3)
    source = "https://maps.googleapis.com/maps/api/staticmap?center=London,EN&size=420x580&maptype=roadmap&zoom=11&"
    source+=markers
    
    source+="&key=AIzaSyAXk7HN8SgkQqfNtRWcWEa1oEJVq3FXI5E"        #for googleMap static api 

    return render_template("index.html", cafes=all_cafes, nbre_lignes=nbre_lignes,nbre_el=len(all_cafes), source=source)


