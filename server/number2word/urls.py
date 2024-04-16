# -*- coding: utf-8 -*-
from django.urls import path

from .views import get, post

urlpatterns = [
    path(
        "sync/<str:number>",
        get,
        name="num_to_english",
    ),
    path(
        "async/",
        post,
        name="num_to_english",
    ),
]
