# Steam signin system with Django and Vue.js

First two steps are common to all buildings and run methods.

## Environment variables

You'll need to change name to the ".env.template" file to ".env" and fill all the empty fields:
- SECRET_KEY: your Django project secret key
- STEAM_API_KEY: your Steam secret key
- ABSOLUTE_URL: uncomment (#) the variable you want to use and comment or delete the others
 - 0.0.0.0 (with docker)
 - 127.0.0.1 (without docker)
 - your domain if you have one

Also you may want to set up some features:

- DEBUG: flag for development builds 
- USE_SSL: flag to use SSL certificates (view next point)
- USE_POSTGRES: flag that sets up postgres database instead of defualt sqlite
- APP_PORT: choose the port you prefer
- ABSOLUTE_URL: choose between DOCKER_URL, LOCAL_URL or DOMAIN_URL values based on how you run the application
- EMAIL_PORT: setting for the email server (NOT USED FOR NOW)
- EMAIL_HOST: setting for the email server (NOT USED FOR NOW)
- POSTGRES_USER: the database user (USE_POSTGRES must be True)
- POSTGRES_PASSWORD: the database password (USE_POSTGRES must be True)
- POSTGRES_PORT: the database port (USE_POSTGRES must be True)

## SSL certificate (for HTTPS)

Feel free to use any tutorial on the internet to create your certificate, here is the one I followed:
https://timonweb.com/django/https-django-development-server-ssl-certificate/
Put both cert and key files inside the "django-steam-vue/backend" folder.

## Build and run with Docker Compose

Docker Compose takes care of setting up anything you need.

Download the CLI tool or the Docker application from their website: https://www.docker.com and Docker Compose as well.

Open the "django-steam-vue" folder in the terminal and run:

`docker-compose up -d --build`

### Enjoy

Open your favourite browser at http://localhost:8000 if you didn't change any option in the env file.

Add an "s" after "http" if you set only USE_SSL.

Change the domain and the port accordingly with the changes you made.

# Without Docker Compose

You need to set up anything by hand.

Still you can choose to run the backend in Docker or locally.

## With Docker

Download the CLI tool or the Docker application from their website: https://www.docker.com.

Open the terminal and navigate to the "django-steam-vue/backend" folder and run this command to build and run the server:

`chmod +x runwithdocker.sh && ./runwithdocker.sh`

## Without Docker

If you don't want to use Docker and run the server on the terminal follow this steps.

Be sure to have python3 installed.

This script will upgrade pip, install a virtual environemnt library, activate it and 

`chmod +x runwithdocker.sh && ./runwithdocker.sh`

Note: to stop the environment type "deactivate"

### Install dependencies and migrate the server

The start.sh script will execute all commands to install our dependencies, migrate and the server.

In the terminal navigate to the "django-steam-vue/backend" folder and run this command:

`chmod +x scripts/start.sh && ./scripts/start.sh`

### Create admin user

The start.sh script will start the server, if you want to create an admin you have to stop it (CTRL-C) and run this command:

`python manage.py createsuperuser`

You'll be asked for the admin credentials.

After you start the server, you can enter the admin section by visiting the path '/admin'.

### Run the server

To start the server run this command in "django-steam-vue/backend":

`chmod +x scripts/run.sh && ./scripts/run.sh`

## Enjoy

After anything went well, you may open your browser at:

- https://0.0.0.0/8000 if you ran Django in Docker

- https://localhost/8000 if you ran Django in the terminal and used SSL

- http://localhost/8000 if you didn't use SSL
