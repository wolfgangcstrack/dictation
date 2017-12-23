""" conftest.py

Fixtures that can be shared across different tests should be defined here.
"""

from datetime import datetime
from pytest import fixture


@fixture
def comprehensive_schema():
    """ Returns a dict that functions as a "schema" to validate dicts against.

    This fixture should be used for comprehensive tests, while tests on the
    special cases listed here should use a separate fixture for better test
    isolation.

    Any new case, especially "special" cases, should be added here.
    """
    return {
        # Some primitive test fields
        'bool field': bool,
        'datetime field': datetime,
        'float field': float,
        'int field': int,
        'list field': list,
        'str field': str,
        # Special cases
        'field that should not be defined': None,
        'list of elements of only one type': [bool],
        'list of elements of varied types': [bool, int],
        'optional field': (bool, None),
        'varied-type field': (bool, int),
        'varied-type optional field': (bool, int, None),
        # Special special cases!!!
        'functionally validated field': lambda v: bool(v),
        'object field with nested fields to be checked': {
            'nested required field': int,
            'nested optional field': (int, None),
        },
    }
