# -*- coding: utf-8 -*-
from django.http import JsonResponse
from rest_framework import status


def validation_error(number: str | int | float) -> JsonResponse:
    """
    Generate a 400 Bad Request error for validation
    issues with an engaging and clear message.
    """
    message = (
        f"🚫 Oops! It looks like your input ('{number}') "
        "isn't quite right. Please make sure it's a valid number. 👍"
    )
    return JsonResponse(
        {
            "success": False,
            "error": {
                "message": message,
                "type": "validation_error",
                "help": (
                    "Ensure that the input is a numerical value"
                    " without any non-numeric characters."
                ),
            },
        },
        status=status.HTTP_400_BAD_REQUEST,
    )


def conversion_error(number: str | int | float, message: str) -> JsonResponse:
    """
    Generate a 500 Internal Server Error for
    conversion failures with detailed feedback.
    """
    return JsonResponse(
        {
            "success": False,
            "error": {
                "message": (
                    "😰 We ran into a snag while"
                    f"converting your number ('{number}')"
                    f". Here's what went wrong: {message}"
                ),
                "type": "conversion_error",
                "help": (
                    "Please review the input or contact"
                    " support for further assistance."
                ),
            },
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
