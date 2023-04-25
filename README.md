# Steam signin system with Django and Vue.js

First two steps are common to all buildings and run methods.

## Environment variables

You'll need to change name to the *.env.template* file to *.env* and fill all the empty fields:
- SECRET_KEY: your Django project secret key
- STEAM_API_KEY: your Steam secret key
- ABSOLUTE_URL: based on where you run the application
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
- POSTGRES_HOST: must be the database service name (USE_POSTGRES must be True)

## SSL certificate (for HTTPS)

Feel free to use any tutorial on the internet to create your certificate, here is the one I followed:
https://timonweb.com/django/https-django-development-server-ssl-certificate/
Put both cert and key files inside the *django-steam/backend* folder.

## Build and run with Docker Compose

Docker Compose takes care of setting up anything you need.

Download the *Docker CLI tool* or the *Docker application* (best) and *Docker Compose* from the website: **https://www.docker.com**.

Open the terminal in the *django-steam* folder and run:

If you are on UNIX base OS:

`bash ./compose.sh`

If you are on Windows:

`chmod + x /compose.sh && ./compose.sh`

It may take some time.

Note: to see how it is going you can eather remove the *-d* from the command or open the container logs in the Docker application.

## Build and run with Docker only

Download the *Docker CLI tool* or the *Docker application* (best) from the website: **https://www.docker.com**.

Open the terminal in the *django-steam* folder and run this script to build and run the server:

If you are on UNIX base OS:

`bash ./backend/run_docker.sh`

If you are on Windows:

`chmod + x /backend/run_docker.sh && ./backend/run_docker.sh`

Note (temporarly): you can **NOT** run postgres in Docker since it prevents containers to communicate (do **NOT** set the **USE_POSTGRES** flag in the *.env* file). If you want to use posgres you have to run the server in the terminal.

## Build and run in the terminal

If you don't want to use Docker at all and run the server in the terminal follow this steps.

Be sure to have python3 installed.

Open the terminal in the *django-steam* folder and run this script to build and run the server:

If you are on UNIX base OS:

`bash ./backend/run_terminal.sh`

If you are on Windows:

`chmod + x /backend/run_terminal.sh && ./backend/run_terminal.sh`

To stop the server use *CRTL-C*, to stop the environment just type *deactivate*.

To restart the server run:

`. venv/bin/activate && bash ./backend/scripts/run.sh True`

## Enjoy

After building finishes and the server is up and running, open your favourite browser at **localhost:8000**.

If you changed the options in the env file:

- Add an *https://* at the start if you set USE_SSL

- Change the domain and the port accordingly with the changes you made

## Other features

### Create admin user

If you are running the server in the terminal, you have to stop it (CTRL-C) then create the superuser and restart the server. The *run.sh* script will start the server.

If you are using Docker with the application, open the server container *django-steam-backend* and go to the *Terminal*.

Once you opened the terminal, run this command in the terminal:

`python manage.py createsuperuser`

You'll be asked for the admin credentials.

After you restarted the server, you can enter the admin section by visiting the path */admin*.
