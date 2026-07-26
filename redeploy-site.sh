#!/bin/bash
set -e

cd /root/pe-portfolio-site

git fetch origin
git reset --hard origin/main

docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build

echo "Redeploy successful: Docker containers rebuilt and started."