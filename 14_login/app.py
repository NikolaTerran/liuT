from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route('/')
def home():
    print(app)
    print(request)
    print(request.args)
    return render_template('home.html')

@app.route('/args')
def check():
    if request.args['usr'] == 'aws' and request.args['pwd']=='aws':
        return render_template('new.html',user=request.args['usr'])
    elif request.args['usr']!='aws' or request.args['pwd']!='aws':
        return render_template('wrongUser.html')
    else: 
        return "i"


app.run(debug=True)
