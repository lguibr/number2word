# -*- coding: utf-8 -*-
import unittest

from number2word.converter import (
    NumberOutOfRangeError,
    convert_integer_to_words,
    convert_three_digit_to_words,
    number_to_words,
)


class TestNumberToWords(unittest.TestCase):
    def setUp(self) -> None:
        self.test_cases: list[tuple[int | str | float, str]] = [
            (0, "zero"),
            ("000000000007", "seven"),
            ("0.0001", "zero point zero zero zero one"),
            (7, "seven"),
            (7e3, "seven thousand"),
            (42, "forty two"),
            (1005, "one thousand five"),
            (
                123456789,
                (
                    "one hundred twenty three million four hundred "
                    "fifty six thousand seven hundred eighty nine"
                ),
            ),
            ("1.5", "one point five"),
            (" -98.7", "minus ninety eight point seven"),
            ("1,000,000", "one million"),
            (
                "1,234,567.89",
                (
                    "one million two hundred thirty four thousand "
                    "five hundred sixty seven point eight nine"
                ),
            ),
            ("1000000000000", "one trillion"),
            ("1000000000000000000000000", "one septillion"),
            (
                "10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,00",
                "one septillion",
            ),
            (
                "1,2,3,4,5,6,7.89",
                (
                    "one million two hundred thirty four thousand "
                    "five hundred sixty seven point eight nine"
                ),
            ),
        ]

        self.fail_cases = [
            ("abc", ValueError),
            ("1000000000000000000000000000000000", NumberOutOfRangeError),
        ]

    def test_number_to_words(self) -> None:
        for number, expected in self.test_cases:
            with self.subTest(number=number):
                self.assertEqual(number_to_words(number), expected)

    def test_fail_cases(self) -> None:
        for number, exception in self.fail_cases:
            with self.subTest(number=number):
                self.assertRaises(exception, number_to_words, number)


class TestIntegerToWords(unittest.TestCase):
    def test_convert_integer_to_words(self) -> None:
        test_cases = [
            ("0", "zero"),
            ("7", "seven"),
            ("42", "forty two"),
            ("105", "one hundred five"),
            ("1005", "one thousand five"),
            (
                "123456789",
                (
                    "one hundred twenty three million four hundred "
                    "fifty six thousand seven hundred eighty nine"
                ),
            ),
            ("1000000000000", "one trillion"),
        ]

        for number, expected in test_cases:
            with self.subTest(number=number):
                self.assertEqual(convert_integer_to_words(number), expected)

    def test_convert_integer_to_words_failures(self) -> None:
        test_cases = [
            ("abc", ValueError),
            (
                "1000000000000000000000000000000000",
                NumberOutOfRangeError,
            ),
            ("1.23", ValueError),
        ]

        for number, exception in test_cases:
            with self.subTest(number=number):
                with self.assertRaises(exception):
                    convert_integer_to_words(number)


class TestThreeDigitNumberToWords(unittest.TestCase):
    def test_convert_three_digit_number_to_words(self) -> None:
        test_cases = [
            ("000", ""),
            ("007", "seven"),
            ("040", "forty"),
            ("015", "fifteen"),
            ("100", "one hundred"),
            ("140", "one hundred forty"),
            ("142", "one hundred forty two"),
        ]

        for number, expected in test_cases:
            with self.subTest(number=number):
                self.assertEqual(
                    convert_three_digit_to_words(number),
                    expected,
                )

    def test_convert_three_digit_number_to_words_failures(self) -> None:
        test_cases = [
            ("1234", ValueError),  # More than three digits
            ("abc", ValueError),  # Invalid characters
        ]

        for number, exception in test_cases:
            with self.subTest(number=number):
                with self.assertRaises(exception):
                    convert_three_digit_to_words(number)


if __name__ == "__main__":
    unittest.main()
