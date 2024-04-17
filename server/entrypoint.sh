#!/bin/bash
# Apply database migrations
echo "Applying database migrations..."
python manage.prod.py makemigrations
python manage.prod.py migrate

# Start Gunicorn with exec to ensure it's the main process
echo "Starting server..."
exec gunicorn server.asgi:application -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --graceful-timeout 1
