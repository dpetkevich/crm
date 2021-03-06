from flask import Flask, request, redirect, make_response, session
from bs4 import BeautifulSoup
import requests
import os
import json
import sys

app = Flask(__name__)

host = 'aiaas.pandorabots.com'
user_key = '8704f84cef67d2c4c1c487ce9aab7da2'
app_id = '1409612152298'
botname = os.environ['BOT_NAME']
crm_username = 'daniel@textbenjamin.com'
crm_pw = 'boris5423:BEN'

@app.route("/boristheanimal5423", methods=['GET','POST'])
def hello():
	


	message = request.values.get('message','hi')
	print 'message'
	print message

	if message.lower() == 'ben':
		message = 'Hi'


	### send message to pandora bots
	query = "https://aiaas.pandorabots.com/atalk/" + str(app_id) + "/" + str(botname) 
	
	payload1 = {
	'user_key' : str(user_key).encode('utf-8'),
	"input": str(message).encode('utf-8')
	}

	pandora_response = requests.post(query, data = payload1)

	full_bot_response = pandora_response.json()

	print 'full bot'
	print full_bot_response

	bot_response = full_bot_response["responses"][0]

	## construct send message request

	url = "https://restapi.crmtext.com/smapi/rest?method=sendsmsmsg"


	payload = {'message':bot_response, 'phone_number': 2812362023}


	response = requests.post(url, params = payload, auth=(crm_username,crm_pw))


	return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)