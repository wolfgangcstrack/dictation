""" test_matches_schema.py

Tests the dictate.matches_schema function for primitive types.
"""

from datetime import datetime
from pytest import fixture

from dictate import matches_schema


@fixture
def primitive_schema():
    return {
        'bool_field': bool,
        'datetime_field': datetime,
        'float_field': float,
        'int_field': int,
        'list_field': list,
        'str_field': str,
    }


def test_matches_none_field():
    """ Test that matches_schema matches against a field that should be None.
    """
    # if field exists and is None, matches_schema returns True
    dict_to_validate = {'none_field': None}
    schema = {'none_field': None}
    assert matches_schema(dict_to_validate, schema)

    # if field exists and is not None, matches_schema returns False
    dict_to_validate = {'none_field': 'not None'}
    assert not matches_schema(dict_to_validate, schema)

    # if field does not exist, matches_schema returns True
    dict_to_validate = {}
    assert matches_schema(dict_to_validate, schema)


def test_matches_primitive_field():
    """ Tests that matches_schema matches against a single primitive field.
    """
    dict_to_validate = {'single_primitive_field': False}
    schema = {'single_primitive_field': bool}
    assert matches_schema(dict_to_validate, schema)

    invalid_dict = {'single_primitive_field': 'not a bool'}
    assert not matches_schema(invalid_dict, schema)


def test_matches_primitive_fields(primitive_schema):
    """ Tests that matches_schema matches against multiple primitive fields.

    Parameters
    ----------
    primitive_schema : dict
        See primitive_schema fixture above.
    """
    dict_to_validate = {
        'bool_field': False,
        'datetime_field': datetime.now(),
        'float_field': 1.0,
        'int_field': 1,
        'list_field': [False, 1, '2', 3.0],
        'str_field': 'I am a str!!!!!',
    }
    assert matches_schema(dict_to_validate, primitive_schema)
