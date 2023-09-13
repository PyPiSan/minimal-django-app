#!/bin/bash
# Prepare log files and start outputting logs to stdout
mkdir -p /app/data/api/

cd /app/
/opt/venv/bin/gunicorn --worker-class=gthread --workers=2 --bind 0.0.0.0:5000 -m 007 --log-level info --access-logfile /app/data/api/gunicorn-access.log --error-logfile /app/data/api/application.log --log-file /app/data/api/application.log --capture-output --reload api.wsgi