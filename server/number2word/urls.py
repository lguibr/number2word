# -*- coding: utf-8 -*-
from django.urls import path

from .views import NumberToEnglishView

urlpatterns = [
    path(
        "<str:number>",
        NumberToEnglishView.as_view(),
        name="num_to_english",
    ),
    path(
        "",
        NumberToEnglishView.as_view(),
        name="num_to_english",
    ),
]
