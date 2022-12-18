# Description

This project contain a Web server/Client that can predict the genre of a music, trained with the GTZAN dataset. 


# Launch the project

Each server can be launch with docker, but the each container can not communicate each other. 
So, only the server predicting will be up, when the client flask will be running.

# Run the main server

To run the main server, you need to run the following command:

```bash
cd server_docker && docker build -t server . && docker run -p 5001:5001 server
cd ..
```

# Run the client

To run the client, you need to run the following command:

```bash
export FLASK_APP=app.py && flask run
```

Then, you can go to the following url: http://localhost:5000/, and upload one of the music contained in the the dataset.

# Train the model

If you want to train the model, you need to download the following dataset 
Link: https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification
Extract it, and run the following command:

```bash
python3 server_docker/src_server/create_model.py <path_to_dataset>/genres_original/
```

Notes: if you have already have "data_mfcc.json", you can pass it to the script, to avoid to recompute it.
