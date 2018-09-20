from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
        <h1>Hello!<h1>
        <a href='/next'>Please visit the next page</a> """

@app.route('/next')
def hasif():
    return """<h1>Hello again!<h1>
        <a href='/next2'>Please visit the last page</a>"""

@app.route('/next2')
def route3():
    return """<h1>Hello once more!<h1>
        <a href="www.youtube.com">Please don't click on this link</a>"""

app.debug = True
app.run()

