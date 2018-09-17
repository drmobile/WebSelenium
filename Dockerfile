FROM joyzoursky/python-chromedriver:2.7-selenium

RUN easy_install pip
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# install Code2000 Font Set
WORKDIR /root/.fonts
RUN wget https://gschoppe.com/projects/fbformat/includes/unicodefont.zip; unzip unicodefont.zip; rm unicodefont.zip
RUN fc-cache -fv

WORKDIR /var/WebSelenium

COPY . .
