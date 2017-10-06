## SI 364
## Fall 2017
## HW 3

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided inside the HW3Part1/templates directory).

from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/artistform')
def artist_form():
 	return render_template('artistform.html')

@app.route('/artistinfo')
def artist_info():
	result = request.args
	chosen_artist = result.get('artist')
	base_url = "https://itunes.apple.com/search?term=" 
	url = base_url + str(chosen_artist)
	x = requests.get(url).text
	return render_template('artist_info.html', objects = json.loads(x)["results"])

@app.route('/artistlinks')
def artist_links():
	return render_template("artist_links.html")

@app.route('/specific/song/<artist_name>')
def specific_song(artist_name):
	base_url = "https://itunes.apple.com/search?term=" 
	url = base_url + str(artist_name)
	x = requests.get(url).text
	return render_template("specific_artist.html", results = json.loads(x)["results"])

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)
