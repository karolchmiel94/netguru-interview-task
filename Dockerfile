FROM python:3.8

# create and set working directory
RUN mkdir /app
WORKDIR /app

# directory code to working directory
ADD . /app/

# default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV PORT=8888

# system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    python3-setuptools \
    python3-pip \
    python3-dev \
    python3-venv \
    git \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# environment dependencies
RUN pip3 install --upgrade pip

# project dependencies
RUN pip install -r /app/requirements.txt

# collect static and make migrations
RUN python manage.py collectstatic --no-input
RUN python manage.py makemigrations && python manage.py migrate

EXPOSE 8888
CMD gunicorn app.wsgi:application --bind 0.0.0.0:$PORT