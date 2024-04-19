# -*- coding: utf-8 -*-
import json
from typing import cast

from django.test import AsyncClient, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class NumberToEnglishTests(APITestCase):
    def test_get_valid_numbers(self) -> None:
        """Test the GET method with various valid numbers."""
        test_cases = [
            (
                "123",
                "one hundred twenty three",
                "Simple hundred-level number",
            ),
            (
                "456",
                "four hundred fifty six",
                "Mid-range hundred-level number",
            ),
            (
                "789",
                "seven hundred eighty nine",
                "High hundred-level number",
            ),
        ]
        for number, expected, title in test_cases:
            with self.subTest(number=number, title=title):
                url = reverse("num_to_english", kwargs={"number": number})
                response = self.client.get(url)
                self.assertEqual(
                    response.status_code,
                    status.HTTP_200_OK,
                    f"Failed: {title}",
                )
                self.assertJSONEqual(
                    response.content,
                    {"success": True, "data": {"num_in_english": expected}},
                    f"Content mismatch: {title}",
                )

    def test_get_invalid_numbers(self) -> None:
        """Test the GET method with various invalid numbers."""
        invalid_numbers = [
            ("abc", "Alphabetic input"),
            ("123abc", "Alphanumeric input"),
            ("!@#$", "Special characters input"),
        ]
        for number, title in invalid_numbers:
            with self.subTest(number=number, title=title):
                url = reverse("num_to_english", kwargs={"number": number})
                response = self.client.get(url)
                self.assertEqual(
                    response.status_code,
                    status.HTTP_400_BAD_REQUEST,
                    f"Failed: {title}",
                )
                self.assertJSONEqual(
                    response.content,
                    {
                        "success": False,
                        "error": {
                            "message": (
                                "🚫 Oops! It looks"
                                f" like your input ('{number}')"
                                " isn't quite right. Please "
                                "make sure it's a valid number. 👍"
                            ),
                            "type": "validation_error",
                            "help": (
                                "Ensure that the input is "
                                "a numerical value without"
                                " any non-numeric characters."
                            ),
                        },
                    },
                    f"Content mismatch: {title}",
                )


class AsyncNumberToEnglishTests(TestCase):
    async def test_post_valid_numbers(self) -> None:
        """Test the POST method with various valid numbers."""
        client = AsyncClient()
        test_cases = [
            (
                "210",
                "two hundred ten",
                "Low two-hundred level number",
            ),
            (
                "321",
                "three hundred twenty one",
                "Mid three-hundred level number",
            ),
            (
                "432",
                "four hundred thirty two",
                "Low four-hundred level number",
            ),
        ]
        for number, expected, title in test_cases:
            with self.subTest(number=number, title=title):
                url = reverse("num_to_english")
                response = await client.post(
                    url,
                    data=json.dumps({"number": number}),
                    content_type="application/json",
                )
                self.assertEqual(
                    response.status_code,
                    status.HTTP_200_OK,
                    f"Failed: {title}",
                )
                self.assertJSONEqual(
                    str(response.content, encoding="utf8"),
                    {"success": True, "data": {"num_in_english": expected}},
                    f"Content mismatch: {title}",
                )

    async def test_post_invalid_numbers(self) -> None:
        """Test the POST method with various invalid numbers."""
        client = AsyncClient()
        invalid_numbers = [
            ("def", "Alphabetic input"),
            ("456def", "Alphanumeric input"),
            ("(*&^%", "Special characters input"),
        ]
        for number, title in invalid_numbers:
            with self.subTest(number=number, title=title):
                url = reverse("num_to_english")
                response = await client.post(
                    url,
                    data=json.dumps({"number": number}),
                    content_type="application/json",
                )
                self.assertEqual(
                    response.status_code,
                    status.HTTP_400_BAD_REQUEST,
                    f"Failed: {title}",
                )
                self.assertJSONEqual(
                    cast(str, response.content),
                    {
                        "success": False,
                        "error": {
                            "message": (
                                "🚫 Oops! It looks like"
                                f" your input ('{number}')"
                                " isn't quite"
                                " right. Please make sure"
                                " it's a valid number. 👍"
                            ),
                            "type": "validation_error",
                            "help": (
                                "Ensure that the input is a numerical value "
                                "without any non-numeric characters."
                            ),
                        },
                    },
                    f"Content mismatch: {title}",
                )
