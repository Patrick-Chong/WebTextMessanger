import os
from twilio.rest import Client
from flask import Flask, render_template


def sendText(destination, message):
	account_sid = 'AC57b907873c59cedaa86df828c55b9e2c'
	auth_token = 'e81135ee4d8651efc660f6d4711071c5'
	client = Client(account_sid, auth_token)

	message = client.messages \
	    .create(
	         body=message,
	         from_='+19896608631',
	         to=destination
	     )

	print(message.sid)


def main(): 
	return render


if __name__ == "__main__": 
	main()