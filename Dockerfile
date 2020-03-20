FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src
ADD . /src

RUN pip install -r requirements.txt

RUN ./manage.py migrate

CMD gunicorn hello_world.wsgi -b 0.0.0.0:3013

EXPOSE 3013