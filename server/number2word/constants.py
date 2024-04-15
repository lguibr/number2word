# -*- coding: utf-8 -*-
import re


class NumberOutOfRangeError(Exception):
    """Exception raised when a number is out of the supported range."""

    pass


DIGIT_GROUP = re.compile(r"(\d{1,3})(?=(\d{3})*(?!\d))")
DECIMAL_POINT = re.compile(r"\.")
VALID_NUMBER = re.compile(r"^-?\d+(,\d{3})*(\.\d+)?$")

UNITS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

TEENS = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
TENS = [
    "",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
THOUSANDS = [
    "",
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
]
