# -*- coding: utf-8 -*-
import json

from asgiref.sync import sync_to_async
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.request import Request

from .converter import number_to_words
from .error_handlers import conversion_error, validation_error
from .serializers import NumberRequestSerializer, NumberResponseSerializer


@require_http_methods(["GET"])
def get(request: Request, number: int) -> HttpResponse:
    return handle_number(request, number)


@csrf_exempt  # Remove to deploy
@require_http_methods(["POST"])
async def post(request: Request) -> HttpResponse:
    try:
        data = json.loads(request.body)
        number_str = data.get("number", "")
    except json.JSONDecodeError:
        error_message = "Invalid JSON data"
        return HttpResponse({"error": error_message}, status=400)
    except ValueError:
        error_message = f"Invalid input {number_str}"
        return HttpResponse({"error": error_message}, status=400)
    response = await sync_to_async(handle_number)(request, number_str)
    return response


def handle_number(request: Request, number: int) -> HttpResponse:
    serializer = NumberRequestSerializer(data={"number": number})
    if serializer.is_valid():
        try:
            number = serializer.validated_data["number"]
            words = number_to_words(number)
            response = NumberResponseSerializer({"num_in_english": words})
            response_data = response.data
            return HttpResponse(
                {"success": True, "data": response_data},
                status=200,
            )
        except Exception as e:
            return conversion_error(number, str(e))
    else:
        return validation_error(str(number))
