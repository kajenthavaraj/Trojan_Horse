FROM python:3.8-slim-buster

WORkDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["wget", "wget https://chromedriver.storage.googleapis.com/<VERSION>/chromedriver_linux64.zip"]

CMD ["unzip chromedriver_linux64.zip"]

COPY main.py .

CMD ["python3", "main.py"]