#!/usr/bin/env bash
# run this with chmod +x runwithoutdocker.sh && ./runwithoutdocker.sh

set -o errexit # exit when a command fails (add "|| true" to commands that you allow to fail)
set -o pipefail # prevents errors in a pipeline from being masked
set -o nounset #  exit when your script tries to use undeclared variables
set -o xtrace # trace what gets executed (useful for debugging)

pip install --upgrade pip

pip install virtualenv

virtualenv env

. env/bin/activate

pip install -r ./requirements.txt

chmod +x scripts/start.sh && ./scripts/start.sh
