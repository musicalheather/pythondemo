#!/bin/bash -x

printenv | sed 's/^\(.*\)$/export \1/g' > /app/project_env.sh

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:80
#echo hi
