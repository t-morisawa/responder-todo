FROM python:3.7-slim

RUN apt-get update && apt-get install -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./src/requirements.txt /app

RUN pip install -r requirements.txt

COPY ./src /app

CMD python app.py
