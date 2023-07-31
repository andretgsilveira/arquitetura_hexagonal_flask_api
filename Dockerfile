FROM python:3.9-slim

WORKDIR /app

COPY ./services/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

