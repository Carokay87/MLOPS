# start by pulling the python image
FROM python:3.10
# switch working directory
WORKDIR /app
# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

RUN apt-get update
RUN apt install -y libsndfile1


# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

EXPOSE 5000


CMD [ "flask", "run", "--host=0.0.0.0", "--port=5001"]