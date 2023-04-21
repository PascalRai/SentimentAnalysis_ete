FROM python:3.9-slim-buster

WORKDIR /sentiment_app

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "sentiment_app.py"]
