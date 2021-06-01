#!/bin/bash -x

printenv | sed 's/^\(.*\)$/export \1/g' > /app/project_env.sh

python3 tempconvert/main.py 0.0.0.0:8080
