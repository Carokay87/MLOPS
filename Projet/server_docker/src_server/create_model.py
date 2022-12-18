from prediction import ModelPrediction
import os
import sys
from extract_data import save_mfcc
from sklearn.metrics import ConfusionMatrixDisplay
from load_data import number_to_labels
import matplotlib.pyplot as plt
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 create_model.py <path_to_dataset> or <path_to_json>") 
        exit(1)
    path_input = sys.argv[1]
    #check if path is a file or a directory
    model = ModelPrediction()
    if os.path.isdir(path_input):

        pred,y_test, genre  = model.train_from_dataset(path_input)
    else:
        pred,y_test, genre  = model.train_from_json(path_input)
    ConfusionMatrixDisplay.from_predictions(number_to_labels(y_test,genre), number_to_labels(pred,genre), labels=genre).plot()
    plt.savefig("confusion_matrix.png")
    model.save_model("model.h5")


