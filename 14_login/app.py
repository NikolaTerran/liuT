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
	print("xxx DIAG:session xxx")
	print(session)
	if "username" in session:
		return render_template('welcome.html',user = session['username'])
	else:
		return render_template('home.html')

@app.route('/login')
def login():
	if request.args['usr'] == 'Alan Smith' and request.args['pwd']=='password12345678':
		print("xxx DIAG:args xxx")
		print(request.args)
		print("xxx DIAG:form xxx")
		print(request.form)
		session['username'] = "Alan Smith"
		print("xxx DIAG:session xxx")
		print(session)
		return redirect(url_for('home'))
	elif request.args['usr'] == 'Alan Smith' and request.args['pwd']!='password12345678':
		return render_template('error.html',message='password wrong!')
	else:
		return render_template('error.html',message='username wrong!')

@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('home'))

	
if __name__ == "__main__":
	app.run(debug=True)
