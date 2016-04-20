FROM python:2.7

WORKDIR /project

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN pip install gunicorn

ADD . /project

CMD gunicorn --bind 0.0.0.0:5000 -w 4 netgram.wsgi

EXPOSE 5000