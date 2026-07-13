#!/bin/bash
set -e

cd /root/pe-portfolio-site

git fetch origin
git reset --hard origin/main

source python3-virtualenv/bin/activate
pip install -r requirements.txt

systemctl restart myportfolio.service
systemctl --no-pager --full status myportfolio.service

echo "Redeploy successful: myportfolio service restarted."