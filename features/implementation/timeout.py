from pytest_bdd import given, parsers


@given(parsers.parse('timeout {timeout:d} seconds'), target_fixture='timeout')
def setup_timeout(timeout):
    return timeout
