import json
import numpy as np


def load_data(path: str):
	"""
	Loads data from json file.
	:param path: Path to json file.
	:return: Dictionary containing data.
	"""
	with open(path, "r") as fp:
		data = json.load(fp)
	inputs = np.array(data["mfcc"])
	targets = np.array(data["labels"])
	genre = np.array(data["mapping"])
	return inputs, targets, genre


def number_to_labels(targets, labels):
	"""
	Converts numeric labels to their corresponding string labels.
	:param targets: Numeric labels.
	:param labels: List of string labels.
	:return: String labels.
	"""
	return [labels[i] for i in targets]