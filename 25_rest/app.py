from flask import *
import urllib.request, urllib.parse, urllib.error
import os
import json

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route("/image")
def process():
	pic = request.args["pic"]
	print(pic)
	response = urlopen("https://img2txt.p.mashape.com/img2txt?encode=true&text=mono",
  headers={
    "X-Mashape-Key": "KbWzilSECimshHJ2CmQxW9rLsKxHp1qA6pWjsnU2HaPabXQ10A",
    "X-Textart-Api-Secret": "<required>"
  },
  params={
    "image": open(pic, mode="r")
  }
)
	return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
