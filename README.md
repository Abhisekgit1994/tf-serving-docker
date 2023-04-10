## Running tfserving through docker

docker run -p 8501:8501 --name tfserving_classifier 
--mount type=bind,source={MODEL_PATH},target=/models/img_classifier 
-e MODEL_NAME=img_classifier -t tensorflow/serving:latest-gpu

-p 8501:8501: This is the REST Endpoint port. Every prediction request will be made to this port. 
For instance, you can make a prediction request to http://localhost:8501.

— name tfserving_classifier: name for the docker container running tfserving. 
It can be used to start and stop the container instance.

— mount type=bind,source={MODEL_PATH},target=/models/img_classifier: 
The mount command simply copies the model from the specified path (MODEL_PATH) into the Docker container (/models/img_classifier).

-e MODEL_NAME=img_classifier: The name of the model folder.

-t tensorflow/serving:latest-gpu: The TF Serving Docker container to run.

###### Thank you for visiting my profile.