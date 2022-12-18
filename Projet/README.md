# Description

This project contain a Web server/Client that can predict the genre of a music. 

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
