#!/usr/bin/env bash

set -o errexit # exit when a command fails (add "|| true" to commands that you allow to fail)
set -o pipefail # prevents errors in a pipeline from being masked
set -o nounset #  exit when your script tries to use undeclared variables
set -o xtrace # trace what gets executed (useful for debugging)

pip install --upgrade pip

pip install virtualenv

virtualenv env

. env/bin/activate

pip install -r ./requirements.txt

export $(grep -v '^#' ../.env | xargs)

if [ ${USE_POSTGRES} = 'True' ]
then
    docker run --name ${POSTGRES_NAME} -p 4321:${POSTGRES_PORT} -e POSTGRES_USER=${POSTGRES_USER} -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} -d postgres
fi

python manage.py makemigrations users
python manage.py makemigrations
python manage.py migrate users
python manage.py migrate

# python manage.py collectstatic --noinput --verbosity 0

bash ./scripts/run.sh
