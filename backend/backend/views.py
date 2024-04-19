# -*- coding: utf-8 -*-
import json
import os

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render


def swagger_view(request):
    path = os.path.join(settings.BASE_DIR, "./static/swagger.json")
    with open(path, "r") as file:
        data = json.load(file)
    return JsonResponse(data)


def swagger_ui_view(request):
    return render(request, "./swagger_ui.html")
