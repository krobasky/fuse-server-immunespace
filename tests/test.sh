#!/bin/bash

set -a
source .env
set +a

docker-compose -f docker-compose.yml -f tests/docker-compose.yml up --build -V --exit-code-from fuse-server-immunespace
