from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def init():
    return render_template('index.html')

@app.route('/output')
def respond():
    print (request)
    print (request.headers)
    print (request.method)
    print (request.args)
    print (request.form)
    return render_template('response.html',response=request.args.get('username'),method=request.method)

if __name__ == '__main__':
    app.run(debug=True)
