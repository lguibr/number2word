FROM python:3.11



WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements/prod.txt

EXPOSE 8000
CMD ["python", "manage.prod.py", "runserver", "0.0.0.0:8000"]
