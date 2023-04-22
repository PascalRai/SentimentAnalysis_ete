FROM python:3.9-slim-buster

WORKDIR /sentiment_app

COPY . .

RUN apt-get update &&\
 apt-get install nano -y &&\
 apt-get install -y libpq-dev &&\
 apt-get install build-essential -y
 
RUN pip install -r requirements.txt

CMD ["python3","run.py"]
