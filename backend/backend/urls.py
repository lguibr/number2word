# -*- coding: utf-8 -*-
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

from .views import swagger_ui_view, swagger_view

urlpatterns = [
    path(
        "",
        lambda request: HttpResponse("OK", status=200),
        name="ecs-health-check",
    ),
    path("admin/", admin.site.urls),
    path("num_to_english/", include("number2word.urls")),
    path("swagger/", swagger_view, name="swagger"),
    path("docs/", swagger_ui_view, name="swagger-ui"),
]
