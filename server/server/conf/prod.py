# -*- coding: utf-8 -*-
import os

from conf.common import *  # noqa: F403 F401
from conf.common import BASE_DIR
from dotenv import load_dotenv

load_dotenv()


DEBUG = os.environ.get("DEBUG")
SECRET_KEY = os.environ.get("SECRET_KEY")
CURRENT_ALLOWED_HOSTS: str | None = os.environ.get("DJANGO_ALLOWED_HOSTS")

if CURRENT_ALLOWED_HOSTS is not None:
    ALLOWED_HOSTS: list[str] = CURRENT_ALLOWED_HOSTS.split(" ")

#  Maybe use PostgreSql on real project conf/prod.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "prod.db.sqlite3",
    }
}
