FROM python:3.9-slim-buster

WORKDIR /sentiment_app

COPY . .

RUN pip install -r requirements.txt

CMD ["python","-m","flask","run","--host=0.0.0.0"]
