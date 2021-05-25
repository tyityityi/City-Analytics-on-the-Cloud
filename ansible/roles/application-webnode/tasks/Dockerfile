FROM python:3.6
COPY ./City-Analytics-on-the-Cloud/Frontend /web-page
COPY ./requirements.txt /web-page
WORKDIR /web-page
#RUN apt-get install curl
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]

