# -*- coding: utf-8 -*-
from django.urls import path

from .views import AsyncNumberPostView, SyncNumberGetView

urlpatterns = [
    path("<str:number>", SyncNumberGetView.as_view(), name="num_to_english"),
    path(
        "",
        AsyncNumberPostView.as_view(),
        name="num_to_english",
    ),
]
