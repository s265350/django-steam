#!/usr/bin/env bash

set -o errexit # exit when a command fails (add "|| true" to commands that you allow to fail)
set -o pipefail # prevents errors in a pipeline from being masked
set -o nounset #  exit when your script tries to use undeclared variables
set -o xtrace # trace what gets executed (useful for debugging)

export $(grep -v '^#' .env | xargs)

if [ ${USE_POSTGRES} = 'True' ]
then
    docker run --name ${POSTGRES_NAME} -p ${POSTGRES_PORT}:5432 -e POSTGRES_USER=${POSTGRES_USER} -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} -d postgres
fi

until docker exec postgres pg_isready ; do sleep 3 ; done

pip install --upgrade pip

pip install virtualenv

virtualenv venv

. venv/bin/activate

pip install -r ./backend/requirements.txt

python backend/manage.py makemigrations users

python backend/manage.py makemigrations

python backend/manage.py migrate

# python backend/manage.py collectstatic --noinput --verbosity 0

bash ./backend/scripts/run.sh True
