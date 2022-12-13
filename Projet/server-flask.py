from src_server import prediction
import logging as log
from enum import Enum
# put mfcc in a additional shape
#enum converter int to genre


log.basicConfig(level=log.DEBUG)
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/analyse", methods=["POST"])
def analyse():
	f = request.files["file"]
	f.save(f.filename)
	# Do the analysis
	return render_template("result.html")
"""

if __name__ == '__main__':
	model_prediction = prediction.ModelPrediction()
	log.info("Training Model")
	model_prediction.train_from_json("data_mfcc.json")
	log.info("Prediction a blues")
	print(model_prediction.predict("data/genres_original/blues/blues.00000.wav"))
	log.info("Saving Model")
	model_prediction.save_model("./model.h5")
	