# CLI commands:
# - docker build . -t backend
# - docker run --name django-backend --env-file ../.env -p 8000:8000 -d backend

# base image
FROM python

# setup working directory
ENV DockerHOME=/app
# create work directory
RUN mkdir -p $DockerHOME
# set work directory (where your code lives)
WORKDIR $DockerHOME
# copy the whole project to your docker home directory
COPY . $DockerHOME

# environment variables
# avoids to write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# doesn't buffer stdin/stdout
ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

# dependencies
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

# port where the Django app runs
EXPOSE ${APP_PORT}

# Fix windows docker bug, convert CRLF to LF and run
#RUN sed -i 's/\r$//g' /app/scripts/start.sh
#CMD chmod +x /app/scripts/start.sh

# run
CMD python manage.py makemigrations users; python manage.py makemigrations; python manage.py migrate users; python manage.py migrate; python manage.py runserver 0.0.0.0:${APP_PORT}
