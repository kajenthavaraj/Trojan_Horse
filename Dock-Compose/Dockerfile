FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN pip3 install selenium
RUN pip3 install selenium chromedriver-binary
RUN pip install --upgrade google-api-python-client
RUN pip3 install google-auth google-auth-oauthlib
RUN pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
RUN pip install --upgrade google-api-python-client

RUN mkdir /app
COPY ./app /app
WORKDIR /app