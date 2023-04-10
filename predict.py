import matplotlib.pyplot as plt
import requests
import json
import numpy as np
from tensorflow.keras.datasets.mnist import load_data

(_, _), (x_test, y_test) = load_data()

# reshape data to have a single channel
x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], x_test.shape[2], 1))
# normalize pixel values
x_test = x_test.astype('float32') / 255.0

# server URL
url = 'http://localhost:8501/v1/models/img_classifier:predict'


def make_prediction(instances):
    data = json.dumps({"signature_name": "serving_default", "instances": instances.tolist()})
    headers = {"content-type": "application/json"}
    json_response = requests.post(url, data=data, headers=headers)
    predictions = json.loads(json_response.text)['predictions']
    return predictions


predictions = make_prediction(x_test[0:4])
# print(predictions)

for i, pred in enumerate(predictions):
    print(f"True Value: {y_test[i]}, Predicted Value: {np.argmax(pred)}")

# docker run -p 8501:8501 --name tfserving_classifier --mount type=bind,source=/Users/tf-server/img_classifier/,target=/models/img_classifier
# -e MODEL_NAME=img_classifier -t tensorflow/serving:latest-gpu