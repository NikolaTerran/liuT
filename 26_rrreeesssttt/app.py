from flask import *
from urllib import request, parse, error
import json

app = Flask(__name__)

@app.route('/')
def home():	
	response = request.urlopen("http://api.icndb.com/jokes/random")		
	info = response.read()	
	dict1 = json.loads(info)
	
	response = request.urlopen("https://www.boredapi.com/api/activity")
	info = response.read()
	dict2 = json.loads(info)

	response = request.urlopen("https://api.adviceslip.com/advice")
	info = response.read()
	dict3 = json.loads(info)

	return render_template("index.html",norris=dict1["value"]["joke"],bored=dict2["activity"],advice=dict3["slip"]["advice"])

if __name__ == "__main__":
    app.run(debug=True)

