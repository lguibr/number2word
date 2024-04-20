# -*- coding: utf-8 -*-
import json
import os

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.request import Request


def swagger_view(request: Request) -> JsonResponse:
    path = os.path.join(settings.BASE_DIR, "static", "swagger.json")
    with open(path, "r") as file:
        data = json.load(file)
    return JsonResponse(data)


def swagger_ui_view(request: Request) -> HttpResponse:
    return render(request, "swagger_ui.html")
