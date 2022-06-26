from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index(): 
	return render_template('index.html')
	

@app.route('/messagerr', methods=["POST","GET"])
def messagerr(): 
	if request.method=="POST": 
		message = request.form['messager']
		return redirect(url_for("messag",msg=message))
	else:
		return render_template('message.html')

@app.route('/<msg>')
def messag(msg): 
	return f"<h1>{msg}</h1>"



if __name__ == "__main__": 
	app.run(debug=True)