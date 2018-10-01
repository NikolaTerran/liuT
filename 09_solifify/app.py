#Terran Liu
#SoftDev1 pd09
#K09 -- Solidify
#2018-10-01    

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return app.send_static_file('index.html')


app.run()
