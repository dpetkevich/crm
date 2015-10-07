from flask import Flask, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/boristheanimal5423", methods=['GET','POST'])
def hello():
	print 'hihi'
	print "url is"
	print request.url
	print "form is "
	print request.form
	print 'json is'
	print request.json
	print 'value are'
	print request.values
	print 'args are'
	print request.args
	print "get_json is"
	print request.get_json
	print "data is"
	print request.data

	return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)