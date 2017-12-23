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
        if isinstance(schema_type, list):
            return _matches_list_with_types(actual_value, schema_type)
        if not _matches_type(actual_value, schema_type):
            return False
    return True


def _matches_list_with_types(value_list, list_with_types):
    """ Helper function for validating value_list against list_with_types.

    Parameters
    ----------
    value_list
        The value_list to check against list_with_types.
    list_with_types : list
        A list of types for which all elements in value_list should be one of.
    """
    if not isinstance(value_list, list):
        return False
    for value in value_list:
        if not any([_matches_type(value, given_type) for given_type in list_with_types]):
            return False
    return True


def _matches_type(value, given_type):
    """ Helper function for validating value against given_type.

    Parameters
    ----------
    value
        The value to check against given_type.
    given_type
        The type for checking value against.
    """
    if given_type is None:
        return value is None
    return isinstance(value, given_type)
