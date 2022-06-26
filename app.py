import os 
from flask import Flask, request, redirect, render_template, Response
from twilio.twiml.messaging_response import MessagingResponse, Message

app = Flask(__name__)


@app.route("/sms", methods=['GET','POST'])
def sms_reply(): 
	resp = MessagingResponse() 

	resp.message("The robots are coming! Head for the hills!")

	return Response(str(resp), mimetype='application/xml')


if __name__ == "__main__": 
	app.run(debug=True)