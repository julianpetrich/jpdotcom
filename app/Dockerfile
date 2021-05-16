FROM python:3.9.1-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV SECRET_KEY secret
ENV CLOUD_NAME name
ENV CLOUD_API_KEY apikey
ENV CLOUD_API_SECRET secret

RUN pip install --upgrade pip
COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

COPY . .

RUN python manage.py collectstatic --noinput