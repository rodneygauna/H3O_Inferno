# Dockerfile
FROM python:3.11-alpine

WORKDIR /app

# install the python packages
COPY requirements.txt /app
RUN --mount=type=cache, target=/root/cache/pip \
	pip3 install -r requirements.txt

# copy the app files and folder to the workdir
COPY . /app

# set the flask environment
ENV FLASK_APP=app

# runs app.py using python3
ENTRYPOINT ["python3"]
CMD ["app.py"]
