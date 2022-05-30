# Dockerfile

# pull the official docker image
FROM python:3.9.4-slim

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# set work directory
WORKDIR /

# Copy app
COPY ./src /src/
COPY ./config /config/

ENTRYPOINT uvicorn src.main:app --host 0.0.0.0