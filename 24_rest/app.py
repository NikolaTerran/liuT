from flask import *
from urllib import request, parse, error
import os
import json

app = Flask(__name__)

@app.route('/')
def home():
	response = request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY")
	html = response.read()
	print(html)
	dict = json.loads(html)
	print(dict)
	return render_template("index.html",url=dict['url'])

if __name__ == "__main__":
    app.run(debug=True)