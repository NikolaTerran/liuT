from flask import *
import urllib.request, urllib.parse, urllib.error
import json

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route("/image")
def process():
	pic = request.args["pic"]
	#pic2 = request.files["pic"]
	param = {'image':open(pic)}
	hdr = {"X-Mashape-Key": "KbWzilSECimshHJ2CmQxW9rLsKxHp1qA6pWjsnU2HaPabXQ10A",
    		"X-Textart-Api-Secret": "<required>"}
	param = {b"image":open(pic,mode="r")}
	req = urllib.request.Request("https://img2txt.p.mashape.com/img2txt?encode=true&text=color",headers=hdr)
	response = urllib.request.urlopen(req)	
	#img = json.loads("textart")
	return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
