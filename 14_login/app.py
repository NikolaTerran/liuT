from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "password12345678"

@app.route('/')
def home():
	print("xxx DIAG:app xxx")
	print(app)
	print("xxx DIAG:request xxx")
	print(request)
	print("xxx DIAG:args xxx")
	print(request.args)
	print("xxx DIAG:form xxx")
	print(request.form)
	if 'alan' in session:
		return render_template('welcome.html',user = request.args['usr'])
	else:
		return render_template('home.html')

@app.route('/login')
def login():
	if request.args['usr'] == 'Alan Smith' and request.args['pwd']=='password12345678':
		session['usr'] = "alan"
		return redirect(url_for('home'))
	elif request.args.get['usr'] == 'Alan Smith' and request.form.get('pwd')!='password12345678':
		return render_template('error.html',message='password wrong!')
	else:
		return render_template('error.html',message='username wrong!')
	

app.run(debug=True)
