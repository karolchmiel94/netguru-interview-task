FROM python:3.8

ADD . /webapp/

WORKDIR /webapp

RUN pip install --upgrade pip

RUN pip install -r /webapp/requirements.txt

RUN python manage.py collectstatic --no-input

RUN python manage.py makemigrations && python manage.py migrate

CMD gunicorn --bind 0.0.0.0:$PORT config.wsgi