""" test_matches_varied_lists.py

Tests the dictation.matches_schema function for fields that have varied list types.
"""

from datetime import datetime
from pytest import fixture

from dictation import matches_schema


@fixture
def varied_lists_schema():
    return {
        'varied_lists_field': ([str], [float], [int, bool], [datetime]),
    }


@fixture
def valid_dicts():
    return [
        {'varied_lists_field': ['we', 'are', 'strings', '!']},
        {'varied_lists_field': [1.0, 2.0, 3.0]},
        {'varied_lists_field': [0, True]},
        {'varied_lists_field': [datetime.now()]},
        {'varied_lists_field': []},
    ]


@fixture
def invalid_dicts():
    return [
        {'varied_lists_field': [(1, 2), ('list', 'of', 'tuples')]},
        {'varied_lists_field': None},
        {},
    ]


def test_matches_varied_lists(valid_dicts, invalid_dicts, varied_lists_schema):
    """ Tests that matches_schema works for varied-type fields.

        Parameters
        ----------
        valid_dicts : list
            See fixture above.
        invalid_dicts : list
            See fixture above.
        varied_lists_schema : dict
            See fixture above.
        """
    assert all(matches_schema(valid_dict, varied_lists_schema) for valid_dict in valid_dicts)
    assert not any(
        matches_schema(invalid_dict, varied_lists_schema) for invalid_dict in invalid_dicts
    )
