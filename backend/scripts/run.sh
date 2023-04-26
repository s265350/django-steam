#!/usr/bin/env bash
# CLI commands:
# - On UNIX: bash ./run.sh
# - On WINDOWS: chmod + x /run.sh && ./run.sh

set -o errexit # exit when a command fails (add "|| true" to commands that you allow to fail)
set -o pipefail # prevents errors in a pipeline from being masked
set -o nounset #  exit when your script tries to use undeclared variables
set -o xtrace # trace what gets executed (useful for debugging)

export $(grep -v '^#' ../../.env | xargs)

if [ ${USE_SSL:-False} = 'True' ]
    then
        if [ ${1:-False} = 'True' ] # first paramerter is set to True when it is colledthe script run_terminal
        then
            python backend/manage.py runserver_plus --cert-file cert.pem --key-file key.pem ${ABSOLUTE_URL:-0.0.0.0}:${APP_PORT:-8000}
        else
            python manage.py runserver_plus --cert-file cert.pem --key-file key.pem ${ABSOLUTE_URL:-0.0.0.0}:${APP_PORT:-8000}
        fi
    else
        if [ ${1:-False} = 'True' ]
        then
            python backend/manage.py runserver ${ABSOLUTE_URL:-0.0.0.0}:${APP_PORT:-8000}
        else
            python manage.py runserver ${ABSOLUTE_URL:-0.0.0.0}:${APP_PORT:-8000}
        fi
    fi
