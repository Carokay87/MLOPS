import keras.optimizers
import numpy as np
from keras import Sequential
from sklearn.model_selection import train_test_split
from load_data import load_data
from keras.layers import Flatten, Dense,Dropout,Conv2D,MaxPool2D,BatchNormalization, Normalization
from extract_data import save_mfcc, get_mfcc_from_path

class ModelPrediction():
	def __init__(self, model_path=None):
		if model_path is not None:
			self.model: Sequential = keras.models.load_model(model_path)
		else:
			self.model : Sequential = None
	
	def predict(self, music_path: str):
		mfcc = get_mfcc_from_path(music_path)
		
		mfcc = np.expand_dims(mfcc, axis=0)
		
		prediction = self.model.predict(mfcc)
		prediction = np.argmax(prediction, axis=1)
		return prediction
	
	
	def train_from_json(self, path):
		inputs, targets, genre = load_data(path)
		X_train, X_test, y_train, y_test = train_test_split(inputs, targets, test_size=0.2)
		self.model = get_model(X_train, y_train, X_test, y_test)
		return np.argmax(self.model.predict(X_test), axis=1),y_test,genre

	def train_from_dataset(self, dataset_path: str):
		save_mfcc(dataset_path, output_path="data_mfcc.json")
		return self.train_from_json("data_mfcc.json")
	
	def save_model(self, path):
		self.model.save(path)


def get_model(train_X, train_Y, test_X, test_Y):
	model = Sequential([
		Conv2D(32, (3, 3), activation='relu', input_shape=(train_X.shape[1], train_X.shape[2], 1)),
		MaxPool2D((3, 3), strides=(2, 2), padding='same'),
		BatchNormalization(),

		Conv2D(32, (3, 3), activation='relu'),
		MaxPool2D((3, 3), strides=(2, 2), padding='same'),
		BatchNormalization(),

		Flatten(),
		Dense(64, activation='relu'),
		Dropout(0.4),

		Dense(10, activation='softmax')
	])
	model.compile(optimizer="adam", loss='sparse_categorical_crossentropy', metrics=['accuracy'])
	model.fit(train_X, train_Y, validation_data=(test_X, test_Y), epochs=24, batch_size=32)
	return model
