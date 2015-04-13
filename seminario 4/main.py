#Jose Antonio Munoz Fuentes

#!/usr/bin/python
# -*- coding: utf-8 -*

__author__ ='Jose Antonio M'
from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

import twitter
import aTwitter 
import io
import json


geocode = '36.525176, -6.287722,100km'

twitter_api = aTwitter.oauth_login()

tweets= twitter_api.search.tweets(q="uca", geocode=geocode) #Buscamos todos los tweets con la palabra "uca" que se hayan enviado cerca de cadiz 
aTwitter.save_json("Ttweets",tweets) #Guardamos la busqueda en un archivo json

Twitter_result = json.loads(open('Ttweets.json').read()) #Leemos el archivo creado anteriormente

lis = []
#creamos una lista con las coordenadas de los tweets encontrados
for result in Twitter_result["statuses"]:
    if result["coordinates"]:
        coordenada = result["coordinates"]
        xy=[coordenada.values()[1][1], coordenada.values()[1][0]]
        lis.append(xy)

app=Flask(__name__)
GoogleMaps(app)


#creamos el mapa
@app.route("/")
def mapview():
    mymap = Map(
        identifier="view-side",
        lat=36.525176,
        lng=-6.287722,
        markers=lis,
        style="height:800px;width:800px;margin:0"
    )
    return render_template('template2.html', mymap=mymap)

if __name__ == "__main__":
    app.run(debug=True) 