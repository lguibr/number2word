# -*- coding: utf-8 -*-
from django.urls import path

from .views import get, post

urlpatterns = [
    path("<str:number>", get, name="num_to_english"),
    path("", post, name="post_num_to_english"),  # type: ignore
]
