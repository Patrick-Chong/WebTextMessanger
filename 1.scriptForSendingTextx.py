import os
from twilio.rest import Client


def sendText(destination, message):
	account_sid = 'AC19ba274fe6cd5b7f61077c3a1a8d14ef'
	auth_token = 'b0a18c66f838747949872fba99db3eeb'
	client = Client(account_sid, auth_token)

	message = client.messages \
	    .create(
	         body=message,
	         from_='+44 7588 743227',
	         to=destination
	     )

	print(message.sid)


def main(): 
	for i in range(10):
		sendText("+447503792398", "Hey zirr")
	return 0


if __name__ == "__main__": 
	main()