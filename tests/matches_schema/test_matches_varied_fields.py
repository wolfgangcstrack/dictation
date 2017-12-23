""" test_matches_schema.py

Tests the dictate.matches_schema function for varied types.
"""

from datetime import datetime
from pytest import fixture

from dictate import matches_schema


@fixture
def list_with_varied_types_schema():
    return {
        'list_field_with_varied_types': [bool, datetime, float, int, list, str]
    }


def test_matches_list_of_varied_types_field(list_with_varied_types_schema):
    """ Tests that matches_schema works for a field that is a varied-type list.

    Parameters
    ----------
    list_with_varied_types_schema : dict
        See list_with_varied_types_schema above
    """
    dict_to_validate = {
        'list_field_with_varied_types': [
            True,
            datetime.now(),
            1.0,
            2,
            [3, 4],
            '5',
        ]
    }
    assert matches_schema(dict_to_validate, list_with_varied_types_schema)

    dict_to_invalidate = {
        'list_field_with_varied_types': 'this is not a list',
    }
    assert not matches_schema(dict_to_invalidate, list_with_varied_types_schema)
