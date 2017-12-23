# dictate
`dictate` is a python module for validating dictionaries based on pre-defined schemas. The need for
something like this arose from the need to validate
[pymongo](https://api.mongodb.com/python/current/) documents in a clean, functional way. ORMs and
ORM-like modules would not fit this requirement due to extra overhead in both execution time and
setup time.

`dictate`'s *schema* structure and validation was inspired by
[Meteor.js' check function](https://docs.meteor.com/api/check.html).

# Usage
```python
from datetime import datetime
import dictate

sample_schema = {
    # Primitive top-level fields in the dict to validate
    'bool_field': bool,
    'datetime_field': datetime,
    'float_field': float,
    'int_field': int,
    'list_field': list,
    'str_field': str,

    # Some special cases
    'field that should not be defined': None,  # will also match None value if key exists in dict to validate
    
    'list of elements of only one type': [bool],
    
    'list of elements of varied types': [bool, int],
    
    'optional_field': (bool, None),
    
    'varied_type_field': (bool, int),
    
    'varied_type_optional_field': (bool, int, None),
    
    'functionally validated field': lambda v: bool(v),
    
    'object field with nested fields to be checked': {
        'nested required field': int,
        'nested optional field': (int, None),
    },
}

valid_dict = {
    'bool_field': True,
    'datetime_field': datetime.now(),
    'float_field': 1.0,
    'int_field': 2,
    'list_field': [3, 4],
    'str_field': "5",
    # 'field that should not be defined': None,  # can uncomment and will still be valid
    'list of elements of only one type': [True, False],
    'list of elements of varied types': [1, True, 0, False],
    # 'optional_field': False,  # can uncomment and will still be valid
    'varied_type_field': int(bool(42)),
    # 'varied_type_optional_field': bool(int('42')),  # can uncomment and will still be valid
    'functionally validated field': 42,
    'object field with nested fields to be checked': {
        'nested required field': 42,
        # 'nested optional field': 42,  # can uncomment and will still be valid
    },
    
    'extra field not in schema': bool(float(int(str(42)))),  # can comment and will still be valid
}

dictate.matches_schema(valid_dict, sample_schema)  # returns True
```

The `sample_schema` above also serves as a reference for what any other schema can contain.
