# -*- coding: utf-8 -*-
import json

from asgiref.sync import async_to_sync, sync_to_async
from django.http import JsonResponse
from django.views import View
from rest_framework.request import Request

from .converter import number_to_words
from .error_handlers import conversion_error, validation_error
from .serializers import NumberRequestSerializer, NumberResponseSerializer


async def async_handle_number(
    request: Request,
    number_str: str,
) -> JsonResponse:
    serializer = NumberRequestSerializer(data={"number": number_str})
    if serializer.is_valid():
        try:
            number = serializer.validated_data["number"]
            words = await sync_to_async(number_to_words)(number)
            response = NumberResponseSerializer({"num_in_english": words})
            response_data = response.data
            return JsonResponse(
                {"success": True, "data": response_data},
                status=200,
            )
        except Exception as e:
            return conversion_error(number_str, str(e))
    else:
        return validation_error(number_str)


class AsyncNumberPostView(View):
    """
    post:
    Convert a number string to words asynchronously.

    Convert a given number in string format to its words
    representation using asynchronous processing.
    """

    async def post(self, request: Request) -> JsonResponse:
        try:
            data = json.loads(request.body)
            number_str = data.get("number", "")
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except ValueError:
            return JsonResponse(
                {"error": f"Invalid input {number_str}"},
                status=400,
            )

        response = await async_handle_number(request, number_str)
        return response


class SyncNumberGetView(View):
    """
    get:
    Convert a number string to words asynchronously.

    Convert a given number in string format to its words
    representation using synchronous processing.
    """

    def get(self, request: Request, number: str) -> JsonResponse:
        return async_to_sync(async_handle_number)(request, number)
