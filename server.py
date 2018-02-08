from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def homePage():
	print request.form
	return render_template("home.html")
@app.route('/form', methods=["POST"])
def form():
	print "Form sent!"
	return redirect("/" + request.form['animal'])
@app.route('/form2', methods=['post'])
def restart():
	print "restarting"
	return redirect('/end')
@app.route('/form3', methods=['post'])
def reincarnation():
	return redirect('/')
@app.route('/otter')
def otterPage():
	return render_template('otter.html')

@app.route('/panda')
def pandaPage():
	return render_template('panda.html')

@app.route('/alpaca')
def alpacaPage():
	return render_template('alpaca.html')

@app.route('/end')
def death():
	return render_template('death.html')

app.run(debug=True)

