# -*- coding: utf-8 -*-
from typing import Callable, cast

from django.http import JsonResponse
from django.urls import path

from .views import AsyncNumberPostView, SyncNumberGetView

urlpatterns = [
    path("<str:number>", SyncNumberGetView.as_view(), name="num_to_english"),
    path(
        "",
        cast(Callable[..., JsonResponse], AsyncNumberPostView.as_view()),
        name="num_to_english",
    ),
]
