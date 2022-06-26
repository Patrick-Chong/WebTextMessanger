import os
from twilio.rest import Client
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index(): 
	return render_template('index.html')


@app.route('/messagerr', methods=["POST","GET"])
def messagerr(destination): 
	account_sid = 'AC57b907873c59cedaa86df828c55b9e2c'
	auth_token = 'e81135ee4d8651efc660f6d4711071c5'
	client = Client(account_sid, auth_token)

	if request.method=="POST": 
		message = request.form['messager']

		message = client.messages \
		    .create(
		         body=message,
		         from_='+19896608631',
		         to=destination
		     )

		return redirect(url_for("messag",msg=message))
	else:
		return render_template('message.html')



@app.route('/<msg>')
def messag(msg): 

	messagerr("+447503792398")

	return 0


if __name__ == "__main__": 
	app.run(debug=True)