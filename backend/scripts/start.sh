#!/usr/bin/env bash

set -o errexit # exit when a command fails (add "|| true" to commands that you allow to fail)
set -o pipefail # prevents errors in a pipeline from being masked
set -o nounset #  exit when your script tries to use undeclared variables
set -o xtrace # trace what gets executed (useful for debugging)

python backend/manage.py makemigrations users
python backend/manage.py makemigrations
python backend/manage.py migrate users
python backend/manage.py migrate

# python manage.py collectstatic --noinput --verbosity 0

bash ./backend/scripts/run.sh
