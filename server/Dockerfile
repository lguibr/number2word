# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements/prod.txt
RUN pip install -r requirements/prod.txt

# Run Django migrations - use the correct management command if not `manage.prod.py`
RUN python manage.prod.py makemigrations
RUN python manage.prod.py migrate

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variables
ENV DJANGO_SETTINGS_MODULE=server.conf.prod

# Start Gunicorn with Uvicorn workers
CMD ["gunicorn", "server.asgi:application", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
