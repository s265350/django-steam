# Steam signin system with Django and Vue.js

## 1. Environment variables

You'll need to change name to the "template.env" file to ".env" and fill all the empty fields:
- SECRET_KEY: your Django project secret key
- STEAM_API_KEY: your Steam secret key
- ABSOLUTE_URL: 0.0.0.0 (with docker) or 127.0.0.1 (without docker)

## 2. SSL certificate (for HTTPS)

You are forced to use SSL certificates ONLY if Django runs in Docker.
Feel free to use any tutorial on the internetto create your certificate, here itis the one I followed: https://timonweb.com/django/https-django-development-server-ssl-certificate/
Put both cert and key files inside the "django-vue/backend" folder.

## 3. Databse setup

You can either use the default sqlite3 database setting or use postgres.

### Sqllite3

There is no futher setup to do forthe database.

### PostgreSQL

Let's start a postgres server in docker (this way it's much simpler to setup).

Just run:

`docker run --name django-vue -p 5432:5432 -e POSTGRES_USER=postgresuser -e POSTGRES_PASSWORD=mysecretpass -d postgres`

You can change port the container name, the user and the password if you wish, but remember to change them also in the env file.

You need to change the database in "django-vue/backend/config/settings.py".

Just switch the commented lines.

```
DATABASES = {
    'default': {
        # sqlite3 DB settings
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # Postgres DB settings
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': env.str('POSTGRES_DB'),
#        'USER': env.str('POSTGRES_USER'),
#        'PASSWORD': env.str('POSTGRES_PASSWORD'),
#        'HOST': env.str('POSTGRES_HOST'),
#        'PORT': env.int('POSTGRES_PORT'),
    },
}
```

## 3. It's better to run in a Docker container

Download the CLI tool or the Docker application from their website: https://www.docker.com.

## 4. With Docker

### Build the image

Open the terminal and navigate to the "django-vue/backend" folder and run this command:

`docker build . -t django-vue`

Building may take sometime.

### Run the container

Run this command in the same folder to start the contianer in detach mode:

`docker run --name django-vue --env-file .env -p 8000:8000 -d django-vue`

It will take some time to be ready after it starts running (check the startus in the container terminal).

If you have the docker application youcan start and stop the container  any time without the terminal.

## 4. Without Docker

If you don't want to use docker but run the server on the terminal follow this steps.
Be sure to have python 3 installed.

#### Virtual environment

It is safer to install the dependencies inside a virtual environment, if you don't care just run the first command.
In the terminal navigate to the "django-vue" folder and run this commands:

`pip install --upgrade pip`

`pip install virtualenv`

`python3 -m venv env`

`source env/bin/activate`

#### Install dependencies and migrate the server

In the terminal navigate to the "django-vue/backend" folder and run this commands:

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

#### Create admin user

To create a server admin run this command and you''lbe prompted for the credentials to login.

`python manage.py createsuperuser`

After you start the server, you can enter the admin section by visiting the path '/admin'.

#### Run the server

If you use SSL the server must be started with this command:

`python manage.py runserver_plus --cert-file cert.pem --key-file key.pem 127.0.0.1:8000`

Else you can just run:

`python manage.py runserver`

If you changed the DOMAIN, ABSOLUTE_URL or APP_PORT in the .env file modify the last part of the first command accordingly.

#### To exit the environment

Stop the server first with CTRL-C then run:

`deactivate`

## 6. Browser

Open your browser and go to:

- https://0.0.0.0/8000 if you ran Django in Docker

- https://localhost/8000 if you ran Django in the terminal and used SSL

- http://localhost/8000 if you didn't use SSL
