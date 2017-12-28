""" test_matches_varied_fields.py

Tests the dictation.matches_schema function for fields that have varied types.
"""

from datetime import datetime
from pytest import fixture

from dictation import matches_schema


@fixture
def function_fields_schema():
    def validating_function(value):
        if isinstance(value, datetime):
            return datetime.now() > value
        return value > 0

    return {
        'functionally_validated_field': validating_function,
    }


@fixture
def valid_dicts():
    return [
        {'functionally_validated_field': 3.0},
        {'functionally_validated_field': 2},
        {'functionally_validated_field': True},
        {'functionally_validated_field': datetime.now()},
    ]


@fixture
def invalid_dicts():
    return [
        {'functionally_validated_field': -2},
        {'functionally_validated_field': -1.0},
        {'functionally_validated_field': False},
    ]


def test_matches_function_fields(valid_dicts, invalid_dicts, function_fields_schema):
    assert all(matches_schema(valid_dict, function_fields_schema) for valid_dict in valid_dicts)
    assert not any(
        matches_schema(invalid_dict, function_fields_schema) for invalid_dict in invalid_dicts
    )
