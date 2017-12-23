""" test_matches_nested_fields.py

Tests the dictate.matches_schema function for nested schema fields.
"""

from datetime import datetime
from pytest import fixture

from dictate import matches_schema


@fixture
def nested_fields_schema():
    return {
        'non_nested_field': bool,
        'nested_fields': {
            'bool_field': bool,
            'datetime_field': datetime,
            'float_field': float,
            'int_field': int,
            'list_field': list,
            'str_field': str,
        },
    }


@fixture
def valid_dict():
    return {
        'non_nested_field': False,
        'nested_fields': {
            'bool_field': True,
            'datetime_field': datetime.now(),
            'float_field': 1.0,
            'int_field': 2,
            'list_field': [3, 4],
            'str_field': '5',
        },
    }


@fixture
def invalid_dict():
    """ This dict is invalid based on the nested_fields being invalid.
    """
    return {
        'non_nested_field': False,  # kept valid here because it is not nested
        'nested_fields': {
            'bool_field': 1,
            'datetime_field': 'Fri Aug 25 1995 00:00:00 GMT-0700 (PDT)',
            'float_field': 1,
            'int_field': 2.0,
            'list_field': (3, 4),
            'str_field': 5,
        },
    }


def test_matches_nested_fields(valid_dict, invalid_dict, nested_fields_schema):
    """ Tests that matches_schema returns true for the given parameters.

    Parameters
    ----------
    valid_dict : dict
        See fixture above.
    invalid_dict : dict
        See fixture above.
    nested_fields_schema : dict
        See fixture above.
    """
    assert matches_schema(valid_dict, nested_fields_schema)
    assert not matches_schema(invalid_dict, nested_fields_schema)
