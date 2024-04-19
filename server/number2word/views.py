# -*- coding: utf-8 -*-
import json

from django.http import JsonResponse
from django.views import View
from rest_framework.request import Request

from .converter import number_to_words
from .error_handlers import conversion_error, validation_error
from .serializers import NumberRequestSerializer, NumberResponseSerializer


class SyncNumberGetView(View):
    def get(self, request: Request, number: int) -> JsonResponse:
        return self.handle_number(request, number)

    def handle_number(self, request: Request, number: int) -> JsonResponse:
        serializer = NumberRequestSerializer(data={"number": number})
        if serializer.is_valid():
            try:
                number = serializer.validated_data["number"]
                words = number_to_words(number)
                response = NumberResponseSerializer({"num_in_english": words})
                response_data = response.data
                return JsonResponse(
                    {"success": True, "data": response_data},
                    status=200,
                )
            except Exception as e:
                return conversion_error(number, str(e))
        else:
            return validation_error(str(number))


class AsyncNumberPostView(View):
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

        response = await self.async_handle_number(request, number_str)
        return response

    async def async_handle_number(
        self, request: Request, number_str: str
    ) -> JsonResponse:
        serializer = NumberRequestSerializer(data={"number": number_str})
        if serializer.is_valid():
            try:
                number = serializer.validated_data["number"]
                words = number_to_words(number)
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
