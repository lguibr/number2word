# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements/prod.txt
RUN pip install --no-cache-dir -r requirements/prod.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variables
ENV DJANGO_SETTINGS_MODULE=backend.conf.prod

# Use an entrypoint script to manage migration commands and start the server
COPY entrypoint.sh /usr/src/app/
RUN chmod +x /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]