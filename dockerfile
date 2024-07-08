FROM python:3.11-alpine3.18

COPY requirements.txt /app/requirements.txt
COPY . /app/
WORKDIR /app

RUN pip install -r /app/requirements.txt

RUN adduser --disabled-password app-user

USER app-user