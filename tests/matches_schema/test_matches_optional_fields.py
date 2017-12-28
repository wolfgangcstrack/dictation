""" test_matches_optional_fields.py

Tests the dictation.matches_schema function for fields that are optional.
"""

from datetime import datetime
from pytest import fixture

from dictation import matches_schema


@fixture
def optional_fields_schema():
    return {
        'bool_field': (bool, None),
        'datetime_field': (datetime, None),
        'float_field': (float, None),
        'int_field': (int, None),
        'list_field': (list, None),
        'str_field': (str, None),
    }


@fixture
def valid_dict():
    # This actually tests for three cases:
    # 1. bool_field is defined and matches the bool type.
    # 2. datetime_field is defined and matches None.
    # 3. All of the other fields are undefined and match None (i.e. optional)
    return {
        'bool_field': True,
        'datetime_field': None,
    }


@fixture
def invalid_dict():
    return {
        'bool_field': 'defined, but not a bool',
    }


def test_matches_optional_fields(valid_dict, invalid_dict, optional_fields_schema):
    """ Tests that matches_schema works for optional fields.

    Parameters
    ----------
    valid_dict : dict
        See fixture above.
    invalid_dict : dict
        See fixture above.
    optional_fields_schema : dict
        See fixture above.
    """
    assert matches_schema(valid_dict, optional_fields_schema)
    assert not matches_schema(invalid_dict, optional_fields_schema)
