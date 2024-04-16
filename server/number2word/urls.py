# -*- coding: utf-8 -*-
from typing import Callable, cast

from django.http import JsonResponse
from django.urls import path

from .views import get, post

urlpatterns = [
    path("<str:number>", get, name="num_to_english"),
    path("", cast(Callable[..., JsonResponse], post), name="num_to_english"),
]
