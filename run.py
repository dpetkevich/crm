from flask import Flask
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/boristheanimal5423")
def hello():
	print request.json
	print request.values
	return "Hello World!"

if __name__ == "__main__":
    app.run()