# -*- coding: utf-8 -*-
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class NumberToEnglishTests(APITestCase):
    def test_get_valid_numbers(self) -> None:
        """Test the GET method with various valid numbers."""
        test_cases = [
            ("123", "one hundred twenty three"),
            ("456", "four hundred fifty six"),
            ("789", "seven hundred eighty nine"),
        ]
        for number, expected in test_cases:
            with self.subTest(number=number):
                url = reverse("num_to_english", kwargs={"number": number})
                response = self.client.get(url)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertJSONEqual(
                    response.content,
                    {"success": True, "data": {"num_in_english": expected}},
                )

    def test_post_valid_numbers(self) -> None:
        """Test the POST method with various valid numbers."""
        test_cases = [
            ("210", "two hundred ten"),
            ("321", "three hundred twenty one"),
            ("432", "four hundred thirty two"),
        ]
        for number, expected in test_cases:
            with self.subTest(number=number):
                url = reverse("num_to_english")
                data = {"number": number}
                response = self.client.post(url, data)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertJSONEqual(
                    response.content,
                    {"success": True, "data": {"num_in_english": expected}},
                )

    def test_get_invalid_numbers(self) -> None:
        """Test the GET method with various invalid numbers."""
        invalid_numbers = ["abc", "123abc", "!@#$"]
        for number in invalid_numbers:
            with self.subTest(number=number):
                url = reverse("num_to_english", kwargs={"number": number})
                response = self.client.get(url)
                self.assertEqual(
                    response.status_code,
                    status.HTTP_400_BAD_REQUEST,
                )
                self.assertJSONEqual(
                    response.content,
                    {
                        "success": False,
                        "error": {
                            "message": (
                                f"Invalid input: {number}. "
                                "Input must be a valid number."
                            ),
                            "type": "validation_error",
                        },
                    },
                )

    def test_post_invalid_numbers(self) -> None:
        """Test the POST method with various invalid numbers."""
        invalid_numbers = ["def", "456def", "(*&^%"]
        for number in invalid_numbers:
            with self.subTest(number=number):
                url = reverse("num_to_english")
                data = {"number": number}
                response = self.client.post(url, data)
                self.assertEqual(
                    response.status_code,
                    status.HTTP_400_BAD_REQUEST,
                )
                self.assertJSONEqual(
                    response.content,
                    {
                        "success": False,
                        "error": {
                            "message": (
                                f"Invalid input: {number}. "
                                "Input must be a valid number."
                            ),
                            "type": "validation_error",
                        },
                    },
                )
