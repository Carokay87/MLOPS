import json
import os
import math
import librosa
from tqdm import tqdm

import logging as log

log.basicConfig(level=log.DEBUG)

DATASET_PATH = "db/"
SAMPLE_RATE = 22050
TRACK_DURATION = 30  # measured in seconds
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION


def get_mfcc_from_path(file_path: str,
		number_sample: int = SAMPLES_PER_TRACK, num_mfcc=13, n_fft=2048,
		hop_length=512):
	signal, sample_rate = librosa.load(file_path, sr=SAMPLE_RATE)
	mfcc = librosa.feature.mfcc(
		y=signal[0:number_sample],
		sr=sample_rate, n_mfcc=num_mfcc,
		n_fft=n_fft,
		hop_length=hop_length)
	return mfcc.T


def save_mfcc(dataset_path, output_path: str = "data_mfcc.json", hop_length = 512):
	"""Extracts MFCCs from music dataset and saves them into a json file along witgh genre labels.
		:param dataset_path (str): Path to dataset
		:param output_path (str): Path to json file used to save MFCCs
		:param num_mfcc (int): Number of coefficients to extract
		:param n_fft (int): Interval we consider to apply FFT. Measured in # of samples
		:param hop_length (int): Sliding window for FFT. Measured in # of samples
		:return:
		"""
	
	# loop through all genre sub-folder
	with tqdm() as pbar:
		# dictionary to store mapping, labels, and MFCCs
		data = {
			"mapping": [],
			"labels": [],
			"mfcc": []
		}
		for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):
			# ensure we're processing a genre sub-folder level
			if dirpath is not dataset_path:
				
				# save genre label (i.e., sub-folder name) in the mapping
				semantic_label = dirpath.split("/")[-1]
				data["mapping"].append(semantic_label)
				print("\nProcessing: {}".format(semantic_label))
				
				# process all audio files in genre sub-dir
				for f in filenames:
					if f.endswith(".wav"):
						pbar.update(1)
						pbar.set_description(f"Processing: {f} ")
						
						# load audio file
						file_path = os.path.join(dirpath, f)
						mfcc = get_mfcc_from_path(file_path, hop_length=hop_length)
						if len(mfcc) == math.ceil(SAMPLES_PER_TRACK / hop_length):
							data["mfcc"].append(mfcc.tolist())
							data["labels"].append(i - 1)
	
	# save MFCCs to json file
	log.info(f"Saving MFCCs to {output_path}")
	with open(output_path, "w") as fp:
		json.dump(data, fp, indent=4)
