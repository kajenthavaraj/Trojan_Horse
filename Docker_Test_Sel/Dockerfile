FROM python:3.9-slim-buster

RUN pip3 install selenium
RUN pip3 install selenium chromedriver-binary
RUN pip install --upgrade google-api-python-client
RUN pip3 install google-auth google-auth-oauthlib
RUN pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
RUN pip install --upgrade google-api-python-client


FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y libu2f-udev && \
    apt-get install -y --no-install-recommends debconf-utils && \
    echo "libu2f-udev libu2f-udev/register-dev-direcory boolean false" | debconf-set-selections && \
    DEBIAN_FRONTEND=noninteractive dpkg-reconfigure -fnoninteractive libu2f-udev && \
    apt-get install -y xvfb && \
    apt-get install -y xorg xvfb gtk2-engines-pixbuf && \
    apt-get install -y dbus-x11 xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic xfonts-scalable && \
    apt-get install -y ffmpeg

ENV sudo apt-add-repository -y ppa:yubico/stable    <- run when with paramiko when intializing virtual machine

# Get chromedriver

RUN apt-get update && apt-get install -y chromium-browser chromium-chromedriver

ENV Xvfb -ac :99 -screen 0 1280x1024x16 && \
    & export DISPLAY=:99

COPY sel_test.py server_run.py
COPY credential.json credential.json

CMD ["python3", "server_run.py", "--nodaemon"]