
#custom image for the fastapi application
FROM python:3
   
ENV PYTHONBUFFERED=1

#create new folder in the container
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY .  /app

EXPOSE 8000







