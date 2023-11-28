# Use an official Python runtime as a parent image
#FROM python:3.9-slim
#
## Set the working directory to /app
#WORKDIR /app
#
## Copy the current directory contents into the container at /app
#COPY . .
#
## Install any needed packages specified in requirements.txt
##RUN pip install --trusted-host pypi.python.org -r requirements.txt
#
# Make port 8000 available to the world outside this container
FROM python:3.11.5-alpine3.18 AS release  
# Create app directory

WORKDIR /app
COPY . .

EXPOSE 8000
#CMD ["sh", "-c", "l"]
#CMD ["python3", "simple-json-server.py"]
