#!/usr/bin/env bash

# run this with chmod +x run.sh && ./run.sh

docker build . -t django-backend
docker run --name django-backend --env-file ../.env -p 8000:8000 -d django-backend
