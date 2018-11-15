from flask import *
from urllib import request, parse, error
import json

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route("/joke")
def process():
	norris = request.args["req"]
	response = request.urlopen("http://api.icndb.com/jokes/random")	
	joke = json.loads("joke")
	return render_template("index.html",chuck=joke)

if __name__ == "__main__":
    app.run(debug=True)
#
