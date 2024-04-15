# -*- coding: utf-8 -*-
from rest_framework import serializers


class NumberRequestSerializer(serializers.Serializer):
    number = serializers.CharField()

    def validate_number(
        self: serializers.Serializer, value: str
    ) -> float | str | Exception:
        try:
            float_value = float(value)
            if float_value.is_integer():
                return int(float_value)
            return float_value
        except ValueError:
            raise serializers.ValidationError("Input must be a valid number.")
        return value


class NumberResponseSerializer(serializers.Serializer):
    num_in_english = serializers.CharField()
