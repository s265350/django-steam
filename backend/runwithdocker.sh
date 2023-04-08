#!/usr/bin/env bash
# run this with chmod +x runwithdocker.sh && ./runwithdocker.sh

set -o errexit # exit when a command fails (add "|| true" to commands that you allow to fail)
set -o pipefail # prevents errors in a pipeline from being masked
set -o nounset #  exit when your script tries to use undeclared variables
set -o xtrace # trace what gets executed (useful for debugging)

docker build . -t django-steam-vue-backend

docker run --name django-steam-vue-backend --env-file ../.env -p 8000:8000 -d django-steam-vue-backend
