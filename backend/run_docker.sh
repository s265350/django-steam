#!/usr/bin/env bash

set -o errexit # exit when a command fails (add "|| true" to commands that you allow to fail)
set -o pipefail # prevents errors in a pipeline from being masked
set -o nounset #  exit when your script tries to use undeclared variables
set -o xtrace # trace what gets executed (useful for debugging)

export $(grep -v '^#' .env | xargs)

docker build . -t django-steam-vue-backend

docker run --name django-steam-vue-backend --env-file ../.env -p ${APP_PORT}:8000 -d django-steam-vue-backend
