FROM python:3.8

RUN pip3 install selenium chromedriver-binary
RUN pip install --upgrade google-api-python-client
RUN pip3 install google-auth google-auth-oauthlib
RUN pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
RUN pip install --upgrade google-api-python-client


COPY test_run.py server_run.py
COPY credential.json credential.json
COPY screenshot.png screenshot.png

CMD ["python3", "server_run.py", "--nodaemon"]