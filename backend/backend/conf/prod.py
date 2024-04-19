# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

from .common import *  # noqa: F403 F401
from .common import BASE_DIR

load_dotenv()


DEBUG = os.environ.get("DEBUG")
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS: list[str] = ["*"]


#  Maybe use PostgreSql on real project conf/prod.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "prod.db.sqlite3",
    }
}
