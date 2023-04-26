#!/usr/bin/env bash
# CLI commands:
# - On UNIX: bash ./run_docker.sh
# - On WINDOWS: chmod + x /run_docker.sh && ./run_docker.sh

set -o errexit # exit when a command fails (add "|| true" to commands that you allow to fail)
set -o pipefail # prevents errors in a pipeline from being masked
set -o nounset #  exit when your script tries to use undeclared variables
set -o xtrace # trace what gets executed (useful for debugging)

export $(grep -v '^#' .env | xargs)

if [ ${USE_POSTGRES:-False} = 'True' ]
then
    docker run --name ${POSTGRES_NAME:-postgres} -p ${POSTGRES_PORT:-4321}:5432 -e POSTGRES_USER=${POSTGRES_USER:-user} -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-pass} -d postgres
    until docker exec postgres pg_isready ; do sleep 3 ; done
fi

docker build backend -t django-steam-vue-backend

docker run --name django-steam-vue-backend --env-file .env -p ${APP_PORT}:8000 -d django-steam-vue-backend
