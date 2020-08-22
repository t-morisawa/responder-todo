FROM python:3.7-slim

# install gcc
RUN apt-get update && apt-get install -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

COPY ./src ./

RUN pip install -r requirements.txt

CMD python app.py
