#!/usr/bin/env bash

set -o errexit # exit when a command fails (add "|| true" to commands that you allow to fail)
set -o pipefail # prevents errors in a pipeline from being masked
set -o nounset #  exit when your script tries to use undeclared variables
set -o xtrace # trace what gets executed (useful for debugging)

export $(grep -v '^#' ../.env | xargs)

pip install --upgrade pip

pip install virtualenv

virtualenv venv

. venv/bin/activate

pip install -r ./backend/requirements.txt

if [ ${USE_POSTGRES} = 'True' ]
then
    docker run --name ${POSTGRES_NAME} -p 4321:${POSTGRES_PORT} -e POSTGRES_USER=${POSTGRES_USER} -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} -d postgres
fi

python backend/manage.py makemigrations users

python backend/manage.py makemigrations

python backend/manage.py migrate

Collect the static files:

python backend/manage.py collectstatic --noinput --verbosity 0

Run the server:

bash ./backend/scripts/run.sh True
