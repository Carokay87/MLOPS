from src_server import prediction
import logging as log
from enum import Enum
from flask import Flask, render_template, request, jsonify


# put mfcc in a additional shape
# enum converter int to genre

class Genre(Enum):
	HIPHOP = 0
	CLASSICAL = 1
	BLUES = 2
	METAL = 3
	JAZZ = 4
	COUNTRY = 5
	POP = 6
	ROCK = 7
	DISCO = 8
	REGGAE = 9


log.basicConfig(level=log.DEBUG)

app = Flask(__name__)

model_prediction = prediction.ModelPrediction("model.h5")


@app.route("/analyse", methods=["POST"])
def analyse():
	f = request.files["file"]
	f.save(f.filename)
	# Do the analysis
	prediction = model_prediction.predict(f.filename)
	genre = Genre(prediction[0]).name
	return jsonify({"genre": genre})


if __name__ == '__main__':
	app.run(debug=True)
