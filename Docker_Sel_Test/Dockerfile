FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN pip3 install selenium


RUN mkdir /app
COPY ./app /app
WORKDIR /app