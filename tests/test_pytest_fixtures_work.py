""" test_pytest_fixtures_work.py

A (simple) test suite that serves as a sanity check for if pytest fixtures are
indeed working.
"""


def test_comprehensive_schema_fixture(comprehensive_schema):
    """ Tests the comprehensive_schema fixture.

    Parameters
    ----------
    comprehensive_schema : dict
        Defined in top-level conftest.py
    """
    assert isinstance(comprehensive_schema, dict)
