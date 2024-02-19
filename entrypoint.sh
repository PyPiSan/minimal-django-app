#!/bin/bash
# Prepare log files and start outputting logs to stdout
mkdir -p /app/data/logs/
touch /app/data/logs/gunicorn.log
touch /app/data/logs/gunicorn-access.log
touch /app/data/logs/application.log
tail -n 0 -f /app/data/logs/application.log &
cd /app/
/opt/venv/bin/gunicorn --worker-class=gthread --workers=2 --bind 0.0.0.0:5000 -m 007 --log-level info --access-logfile /app/data/logs/gunicorn-access.log --error-logfile /app/data/logs/application.log --log-file /app/data/logs/application.log --capture-output --reload app.wsgi