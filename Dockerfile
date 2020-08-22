FROM python:3.7-slim

RUN apt-get update && apt-get install -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

COPY ./src/requirements.txt ./

RUN pip install -r requirements.txt

COPY ./src ./

CMD python app.py
