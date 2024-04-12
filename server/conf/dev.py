import os

from .common import *
from dotenv import load_dotenv

load_dotenv()


DEBUG = os.environ.get("DEBUG")
SECRET_KEY = os.environ.get("SECRET_KEY")
CURRENT_ALLOWED_HOSTS: str | None = os.environ.get("DJANGO_ALLOWED_HOSTS")

if CURRENT_ALLOWED_HOSTS is not None:
  ALLOWED_HOSTS: list[str] = CURRENT_ALLOWED_HOSTS.split(" ")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}