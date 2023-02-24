FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-add-repository -y ppa:yubico/stable

RUN apt-get update && \
    apt-get install -y libu2f-udev && \
    apt-get install -y --no-install-recommends debconf-utils && \
    echo "libu2f-udev libu2f-udev/register-dev-direcory boolean false" | debconf-set-selections && \
    DEBIAN_FRONTEND=noninteractive dpkg-reconfigure -fnoninteractive libu2f-udev && \
    apt-get install -y xvfb && \
    apt-get install -y xorg xvfb gtk2-engines-pixbuf && \
    apt-get install -y dbus-x11 xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic xfonts-scalable && \
    apt-get install -y ffmpeg && \
    apt-get install -y wget && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb 

RUN Xvfb -ac :99 -screen 0 1280x1024x16 & export DISPLAY=:99


FROM python:3.8

COPY piprequirements.txt piprequirements.txt
RUN pip3 install -r piprequirements.txt
RUN pip3 install selenium chromedriver-binary
RUN pip install --upgrade google-api-python-client
RUN pip3 install google-auth google-auth-oauthlib
RUN pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
RUN pip install --upgrade google-api-python-client

COPY server_run.py /app/server_run.py

CMD ["python3", "/app/server_run.py"]