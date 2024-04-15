# -*- coding: utf-8 -*-
from django.urls import path

from .views import NumberToEnglishView

urlpatterns = [
    path(
        "num_to_english/<str:number>",
        NumberToEnglishView.as_view(),
        name="num_to_english",
    ),
    path(
        "num_to_english",
        NumberToEnglishView.as_view(),
        name="num_to_english",
    ),
]
