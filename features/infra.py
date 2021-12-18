import pytest
import testinfra


@pytest.fixture(scope='session')
def local():
    """
    Replace testinfra default 'host'.

    Testinfra's 'host' doesn't work together with pytest-bdd, hence
    this work-around.
    """
    return testinfra.get_host('local://')
