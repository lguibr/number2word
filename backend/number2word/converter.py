# -*- coding: utf-8 -*-
import decimal
import re
from typing import List, Union

from number2word.constants import (
    DECIMAL_POINT,
    DIGIT_GROUP,
    TEENS,
    TENS,
    THOUSANDS,
    UNITS,
    VALID_NUMBER,
    NumberOutOfRangeError,
)


def convert_to_full_decimal(num_str: str) -> str:
    if "e" in num_str or "E" in num_str:
        num_str = f"{decimal.Decimal(num_str):f}"
    return num_str


def number_to_words(number: Union[int, float, str]) -> str:
    original_number = str(number).strip().replace(",", "")
    original_number = convert_to_full_decimal(
        original_number
    )  # Convert scientific notation

    if not VALID_NUMBER.match(original_number):
        raise ValueError(f"Invalid input: {number}")

    if original_number.startswith("-"):
        sign = "minus "
        original_number = original_number[1:]
    else:
        sign = ""

    if DECIMAL_POINT.search(original_number):
        integer_part, decimal_part = original_number.split(".")

        if all(digits == "0" for digits in decimal_part):
            return sign + convert_integer_to_words(integer_part)
        else:
            return (
                sign
                + convert_integer_to_words(integer_part)
                + " point "
                + " ".join(UNITS[int(digit)] for digit in decimal_part)
            )
    else:
        return sign + convert_integer_to_words(original_number)


def convert_integer_to_words(string_number: str) -> str:
    number = string_number.lstrip("0") or "0"
    if not re.fullmatch(r"-?\d+", string_number):
        raise ValueError("Input must be an integer.")
    chunks: List[str] = [match[0] for match in DIGIT_GROUP.findall(number)]

    if number == "0":
        return UNITS[0]

    words = []
    if len(chunks) > len(THOUSANDS) - 1:
        raise NumberOutOfRangeError("Number out of supported range.")

    for index, chunk in enumerate(reversed(chunks)):
        if int(chunk) != 0:
            words_chunk = convert_three_digit_to_words(chunk)
            words.append(words_chunk + " " + THOUSANDS[index])
    return " ".join(reversed(words)).strip()


def convert_three_digit_to_words(string_number: str) -> str:
    number = f"{int(string_number):03d}"
    hundreds, tens, units = map(int, number)
    words = []

    if hundreds:
        words.append(UNITS[hundreds] + " hundred")

    if tens > 1:
        words.append(TENS[tens])
        if units:
            words.append(UNITS[units])
    elif tens == 1:  # Handling tens
        words.append(TEENS[units])
    elif units:
        words.append(UNITS[units])

    return " ".join(words)
