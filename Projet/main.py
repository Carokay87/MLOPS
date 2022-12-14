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
	print("Received file: " + f.filename)
	prediction: requests.Response = requests.post(server_API + "/analyse", files={"file": f})
	
	print(prediction.json()["genre"])
	result = prediction.json()["genre"]
	print(result)
	return render_template("result.html", result=result)


if __name__ == "__main__":
	app.run(debug=True)
