FROM python:3.8

WORKDIR code

ENV PYTHONIOENCODING UTF-8
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV development
ENV FLASK_APP src/app.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements/dev.txt .

RUN pip install --upgrade pip && pip install -r dev.txt

EXPOSE 5000
