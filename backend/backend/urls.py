# -*- coding: utf-8 -*-
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

urlpatterns = [
    path(
        "",
        lambda request: HttpResponse("OK", status=200),
        name="ecs-health-check",
    ),
    path("admin/", admin.site.urls),
    path("num_to_english/", include("number2word.urls")),
]
