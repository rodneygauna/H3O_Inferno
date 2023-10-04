# Dockerfile
FROM python:3.11.6-slim-bookworm

WORKDIR /app

# install the python packages
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

# copy the app files and folder to the workdir
COPY . /app

# set the flask environment
ENV FLASK_APP=app

# runs apt update and upgrade -y
RUN apt update && apt upgrade -y

# install WKHTMLTOPDF
RUN apt install libxrender1 libfontconfig1 libxext6 libx11-6 -y
RUN apt install wkhtmltopdf -y

# install chrome for selenium
RUN apt install chromium -y

# install chromedriver for selenium
RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.92/linux64/chromedriver-linux64.zip
RUN unzip chromedriver-linux64.zip
RUN mv chromedriver /usr/bin/chromedriver
RUN chmod +x /usr/bin/chromedriver

# explose the port 1025
EXPOSE 1025

# runs app.py using python3
ENTRYPOINT ["python3"]
CMD ["app.py"]
