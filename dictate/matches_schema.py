""" matches_schema.py

Given a dict and a schema, validate the dict based on the schema.
"""


def matches_schema(dict_to_validate, schema):
    """ Given a dict and a schema, validate the dict based on the schema.

    Parameters
    ----------
    dict_to_validate : dict
        The dict to validate against schema
    schema : dict
        The schema used to validate dict_to_validate. See documentation for
        details on what the structure of this dict should look like.

    Returns
    -------
    bool
        Whether the dict_to_validate matches the schema or not.
    """
    for field in schema:
        schema_type = schema[field]
        actual_value = dict_to_validate.get(field)

        if isinstance(schema_type, dict):
            if not _matches_dict(actual_value, schema_type):
                return False
        elif isinstance(schema_type, list):
            if not _matches_list(actual_value, schema_type):
                return False
        elif not _matches_type(actual_value, schema_type):
            return False

    return True


def _matches_dict(value_dict, schema_type_dict):
    """ Helper function for validating nested fields.

    Essentially, this recursively calls matches_schema as long as value_dict is
    indeed an instance of dict.

    Parameters
    ----------
    value_dict : dict
        The value to validate against schema_type_dict.
    schema_type_dict : dict
        The dict of schema types (which may also be nested dicts) that
        value_dict will be validated against.
    """
    if not isinstance(value_dict, dict):
        return False
    return matches_schema(value_dict, schema_type_dict)


def _matches_list(value_list, schema_type_list):
    """ Helper function for validating value_list against list_with_types.

    Parameters
    ----------
    value_list : list
        The value_list to check against list_with_types.
    schema_type_list : list
        A list of types for which all elements in value_list should be one of.
    """
    if not isinstance(value_list, list):
        return False
    for value in value_list:
        if not any([_matches_type(value, given_type) for given_type in schema_type_list]):
            return False
    return True


def _matches_type(value, schema_type):
    """ Helper function for validating value against given_type.

    Parameters
    ----------
    value
        The value to check against given_type.
    schema_type
        The type for checking value against.
    """
    if schema_type is None:
        return value is None
    return isinstance(value, schema_type)
