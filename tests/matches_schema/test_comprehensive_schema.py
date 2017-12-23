""" test_comprehensive_schema.py

Tests dictate.matches_schema against the comprehensive_schema fixture. This
fixture includes all schema field types for validating a dict and is located
in 'tests/conftest.py'.
"""

from datetime import datetime
from pytest import fixture
from random import random

from dictate import matches_schema


@fixture
def valid_dict():
    v_dict = {
        'bool_field': True,
        'datetime_field': datetime.now(),
        'float_field': 1.0,
        'int_field': 2,
        'list_field': [3, 4],
        'str_field': '5',
        # 'field that should not be defined': None,  # can be commented/uncommented out and still be valid
        'list of elements of only one type': [True, False],
        'list of elements of varied types': [True, 1, False, 0],
        # 'optional_field': False,  # can be commented/uncommented out and still be valid
        'varied_type_field': int(bool(42)),
        # 'varied_type_optional_field': bool(int('42')),  # can be commented/uncommented out and still be valid
        'functionally validated field': True,
        'object field with nested fields to be checked': {
            'nested required field': 42,
            # 'nested optional field': 42,  # can be commented/uncommented out and still be valid
        },
    }

    # the coin_flip below demonstrates that these fields are optional and matches_schema should
    # validate v_dict correctly regardless of whether they are in the v_dict dict or not
    coin_flip = random() > 0.5
    if coin_flip:
        v_dict['field that should not be defined'] = None
        v_dict['optional_field'] = False
        v_dict['varied_type_optional_field'] = bool(int('42'))
        v_dict['object field with nested fields to be checked']['nested optional field'] = 42

    return v_dict


def test_matches_comprehensive_schema(valid_dict, comprehensive_schema):
    """ Tests valid_dict against comprehensive_schema, mainly for sanity check.
    
    Parameters
    ----------
    valid_dict : dict
        See fixture above.
    comprehensive_schema : dict
        See fixture defined in 'tests/conftest.py'.
    """
    assert matches_schema(valid_dict, comprehensive_schema)
