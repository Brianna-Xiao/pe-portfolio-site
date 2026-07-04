#!/bin/bash

tmux kill-server 2>/dev/null

cd ~/pe-portfolio-site || exit 1

git fetch
git reset --hard origin/main

source python3-virtualenv/bin/activate
pip install -r requirements.txt

tmux new-session -d -s portfolio "cd ~/pe-portfolio-site && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"