#!/usr/bin/env bash
# CLI commands:
# - On UNIX: bash ./compose.sh
# - On WINDOWS: chmod + x /compose.sh && ./compose.sh

set -o errexit # exit when a command fails (add "|| true" to commands that you allow to fail)
set -o pipefail # prevents errors in a pipeline from being masked
set -o nounset #  exit when your script tries to use undeclared variables
set -o xtrace # trace what gets executed (useful for debugging)

unamestr=$(uname)
if [[ "$unamestr" == 'Windows' ]]; then
    export COMMAND="chmod + x /scripts/start.sh && ./scripts/start.sh"
else
    export COMMAND="bash ./scripts/start.sh"
fi

docker-compose up -d --build