# -*- coding: utf-8 -*-
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.views import APIView

from .converter import number_to_words
from .error_handlers import conversion_error, validation_error
from .serializers import NumberRequestSerializer, NumberResponseSerializer


class NumberToEnglishView(APIView):
    def get(self, request: Request, number: int) -> JsonResponse:
        return self.handle_number(request, number)

    def post(self, request: Request) -> JsonResponse:
        number_str = request.data.get("number", "")
        try:
            number = int(number_str)
        except ValueError:
            return validation_error(number_str)
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
                    {"success": True, "data": response_data}, status=200
                )
            except Exception as e:
                return conversion_error(number, str(e))
        else:
            return validation_error(str(number))
