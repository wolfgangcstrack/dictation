""" test_matches_varied_fields.py

Tests the dictation.matches_schema function for fields that have varied types.
"""

from datetime import datetime
from pytest import fixture

from dictation import matches_schema


@fixture
def varied_fields_schema():
    return {
        'varied_field': (bool, datetime, float, int, list, str),
    }


@fixture
def valid_dicts():
    return [
        {'varied_field': True},
        {'varied_field': datetime.now()},
        {'varied_field': 1.0},
        {'varied_field': 2},
        {'varied_field': [3, 4]},
        {'varied_field': '5'},
    ]


@fixture
def invalid_dicts():
    return [
        {'varied_field': tuple()},
        {'varied_field': None},
        {},
    ]


def test_matches_varied_fields(valid_dicts, invalid_dicts, varied_fields_schema):
    """ Tests that matches_schema works for varied-type fields.

    Parameters
    ----------
    valid_dicts : list
        See fixture above.
    invalid_dicts : list
        See fixture above.
    varied_fields_schema : dict
        See fixture above.
    """
    assert all(matches_schema(valid_dict, varied_fields_schema) for valid_dict in valid_dicts)
    assert not any(
        matches_schema(invalid_dict, varied_fields_schema) for invalid_dict in invalid_dicts
    )
