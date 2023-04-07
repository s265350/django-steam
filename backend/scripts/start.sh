#!/usr/bin/env bash

set -o errexit # exit when a command fails (add "|| true" to commands that you allow to fail)
set -o pipefail # prevents errors in a pipeline from being masked
set -o nounset #  exit when your script tries to use undeclared variables
set -o xtrace # trace what gets executed (useful for debugging)

import environ
env = environ.Env()

python manage.py makemigrations users
python manage.py makemigrations
python manage.py migrate users
python manage.py migrate

#python manage.py collectstatic --noinput --verbosity 0

if [ ${env.bool('USE_SSL'):-false} ]
then
  python manage.py runserver
else
  python manage.py runserver_plus ${env.bool('ABSOLUTE_URL')}
fi

#gunicorn config.wsgi -w 4 --worker-class gevent -b 0.0.0.0:8000 --chdir=/app
