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
        self.test_cases = [
            (0, "zero", "Zero as an integer"),
            ("000000000007", "seven", "Leading zeros string"),
            (
                "0.0001",
                "zero point zero zero zero one",
                "Decimal with leading zeros",
            ),
            (7, "seven", "Single digit integer"),
            (7e3, "seven thousand", "Scientific notation"),
            (42, "forty two", "Two-digit number"),
            (
                1005,
                "one thousand five",
                "Four-digit number with unique zero context",
            ),
            (
                123456789,
                (
                    "one hundred twenty three million four hundred"
                    " fifty six thousand seven hundred eighty nine"
                ),
                "Complex nine-digit number",
            ),
            ("1.5", "one point five", "Simple decimal"),
            (" -98.7", "minus ninety eight point seven", "Negative decimal"),
            ("1,000,000", "one million", "Formatted number with commas"),
            (
                "1,234,567.89",
                (
                    "one million two hundred thirty four thousand"
                    " five hundred sixty seven point eight nine"
                ),
                "Complex formatted number with decimals",
            ),
            ("1000000000000", "one trillion", "Large number with trillion"),
            (
                "1000000000000000000000000",
                "one septillion",
                "Very large number with septillion",
            ),
            (
                "10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,00",
                "one septillion",
                "Malformed number formatting",
            ),
            (
                "1,2,3,4,5,6,7.89",
                (
                    "one million two hundred thirty four thousand"
                    " five hundred sixty seven point eight nine"
                ),
                "Improperly formatted large number with decimal",
            ),
        ]

        self.fail_cases = [
            ("abc", ValueError, "Non-numeric string"),
            (
                "1000000000000000000000000000000000",
                NumberOutOfRangeError,
                "Excessively large number beyond range",
            ),
        ]

    def test_number_to_words(self) -> None:
        for number, expected, title in self.test_cases:
            with self.subTest(number=number, title=title):
                self.assertEqual(
                    number_to_words(str(number)), expected, f"Failed: {title}"
                )

    def test_fail_cases(self) -> None:
        for number, exception, title in self.fail_cases:
            with self.subTest(number=number, title=title):
                with self.assertRaises(exception, msg=f"Failed: {title}"):
                    number_to_words(number)


class TestIntegerToWords(unittest.TestCase):
    def test_convert_integer_to_words(self) -> None:
        test_cases = [
            ("0", "zero", "Zero as string"),
            ("7", "seven", "Single digit string"),
            ("42", "forty two", "Two-digit number"),
            ("105", "one hundred five", "Three-digit number"),
            (
                "1005",
                "one thousand five",
                "Four-digit number with unique context",
            ),
            (
                "123456789",
                (
                    "one hundred twenty three million four hundred"
                    " fifty six thousand seven hundred eighty nine"
                ),
                "Complex nine-digit number",
            ),
            ("1000000000000", "one trillion", "Trillion number"),
        ]

        for number, expected, title in test_cases:
            with self.subTest(number=number, title=title):
                self.assertEqual(
                    convert_integer_to_words(number),
                    expected,
                    f"Failed: {title}",
                )

    def test_convert_integer_to_words_failures(self) -> None:
        test_cases = [
            ("abc", ValueError, "Alphabetic string"),
            (
                "1000000000000000000000000000000000",
                NumberOutOfRangeError,
                "Excessively large number",
            ),
            ("1.23", ValueError, "Invalid decimal for integer conversion"),
        ]

        for number, exception, title in test_cases:
            with self.subTest(number=number, title=title):
                with self.assertRaises(exception, msg=f"Failed: {title}"):
                    convert_integer_to_words(number)


class TestThreeDigitNumberToWords(unittest.TestCase):
    def test_convert_three_digit_number_to_words(self) -> None:
        test_cases = [
            ("000", "", "Three zeros"),
            ("007", "seven", "Leading zeros with seven"),
            ("040", "forty", "Two-digit zero lead"),
            ("015", "fifteen", "Two-digit with leading zero"),
            ("100", "one hundred", "Single hundred"),
            ("140", "one hundred forty", "Hundred with forty"),
            ("142", "one hundred forty two", "Full three-digit number"),
        ]

        for number, expected, title in test_cases:
            with self.subTest(number=number, title=title):
                self.assertEqual(
                    convert_three_digit_to_words(number),
                    expected,
                    f"Failed: {title}",
                )

    def test_convert_three_digit_number_to_words_failures(self) -> None:
        test_cases = [
            ("1234", ValueError, "More than three digits"),
            ("abc", ValueError, "Non-numeric string"),
        ]

        for number, exception, title in test_cases:
            with self.subTest(number=number, title=title):
                with self.assertRaises(exception, msg=f"Failed: {title}"):
                    convert_three_digit_to_words(number)


if __name__ == "__main__":
    unittest.main()
