FROM joyzoursky/python-chromedriver:2.7-selenium

WORKDIR /var/WebSelenium

RUN easy_install pip
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . .
