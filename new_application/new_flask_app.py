from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True 

@app.route('/first')
def first():
	return render_template('first.html')

@app.route('/last', methods = ['GET'])
def last():
	result = request.args
	chosen_artist = result.get('options')
	base_url = "https://itunes.apple.com/search?term=" 
	url = base_url + str(chosen_artist)
	x = requests.get(url, params = {"entity": "musicArtist"}).text
	return render_template('last.html', data = json.loads(x)["results"][0]["primaryGenreName"])

if __name__ == '__main__':
    app.run()