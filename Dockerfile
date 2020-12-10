# FROM directive instructing base image to build upon
FROM python:3

# WORKDIR defines /code as the image's working directory
WORKDIR /code

# COPY requirements.txt before rest of repo
COPY requirements.txt /code/
# requirements.txt must be copied before invalidating the
# cache by copying the whole repo to ensure this step only 
# runs when requirements.txt is CHANGED

# RUN a command to install the requirements
RUN pip install -r requirements.txt

# COPY the rest of the application code to the image
COPY . /code/