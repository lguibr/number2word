# -*- coding: utf-8 -*-
from django.http import JsonResponse
from rest_framework import status


def validation_error(number: str | int | float) -> JsonResponse:
    """Generate a 400 Bad Request error for validation issues."""
    message = f"Invalid input: {number}. Input must be a valid number."
    return JsonResponse(
        {
            "success": False,
            "error": {
                "message": message,
                "type": "validation_error",
            },
        },
        status=status.HTTP_400_BAD_REQUEST,
    )


def conversion_error(number: str | int | float, message: str) -> JsonResponse:
    """Generate a 500 Internal Server Error for conversion failures."""
    return JsonResponse(
        {
            "success": False,
            "error": {
                "message": f"Error converting number {number}: {message}",
                "type": "conversion_error",
            },
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
