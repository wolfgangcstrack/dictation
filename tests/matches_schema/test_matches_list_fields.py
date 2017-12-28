""" test_matches_schema.py

Tests the dictation.matches_schema function for varied types.
"""

from datetime import datetime
from pytest import fixture

from dictation import matches_schema


@fixture
def list_with_one_type_schema():
    return {
        'list_field_with_one_type': [str]
    }


@fixture
def list_with_varied_types_schema():
    return {
        'list_field_with_varied_types': [bool, datetime, float, int, list, str]
    }


@fixture
def valid_varied_type_dict():
    return {
        'list_field_with_varied_types': [
            True,
            datetime.now(),
            1.0,
            2,
            [3, 4],
            '5',
        ]
    }


@fixture
def valid_single_type_dict():
    return {
        'list_field_with_one_type': ['we', 'are', 'all', 'strings', '!']
    }


def test_matches_list_of_one_type_field(valid_single_type_dict, list_with_one_type_schema):
    """ Tests that matches_schema works for a field that is a single-type list.

    Parameters
    ----------
    valid_single_type_dict : dict
        See fixture above
    list_with_one_type_schema : dict
        See fixture above
    """
    assert matches_schema(valid_single_type_dict, list_with_one_type_schema)

    invalid_dict = {
        'list_field_with_one_type': ['we', 'are', not all, 'strings', '!']
    }
    assert not matches_schema(invalid_dict, list_with_one_type_schema)


def test_matches_list_of_varied_types_field(valid_varied_type_dict, list_with_varied_types_schema):
    """ Tests that matches_schema works for a field that is a varied-type list.

    Parameters
    ----------
    valid_varied_type_dict : dict
        See fixture above
    list_with_varied_types_schema : dict
        See fixture above
    """
    assert matches_schema(valid_varied_type_dict, list_with_varied_types_schema)

    invalid_dict = {
        'list_field_with_varied_types': 'this is not a list',
    }
    assert not matches_schema(invalid_dict, list_with_varied_types_schema)
