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

# runs app.py using python3
ENTRYPOINT ["python3"]
CMD ["app.py"]
