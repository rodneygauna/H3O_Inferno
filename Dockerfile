FROM python:3.11.6-slim-bookworm

WORKDIR /app

# Install dependencies
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

# Copy app files
COPY . /app

# System packages installation
RUN apt update && apt upgrade -y
RUN apt install libxrender1 libfontconfig1 libxext6 libx11-6 wkhtmltopdf -y
