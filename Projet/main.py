# Basic falsk serveur
from flask import Flask, render_template, request

server_API = "http://localhost:5001"

import requests

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")


@app.route("/uploader", methods=["POST"])
def uploader():
	f = request.files["file"]
	prediction: requests.Response = requests.post(server_API + "/analyse", files={"file": f})
	
	print(prediction.json()["genre"])
	return prediction.json()["genre"]


if __name__ == "__main__":
	app.run(debug=True)
