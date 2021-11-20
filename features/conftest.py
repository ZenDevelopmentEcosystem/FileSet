import pytest
from implementation.fileset import *  # noqa: F403,F401


def pytest_addoption(parser):
    parser.addoption('--fileset-path', action='store', help='Path to fileset.pyz')
    parser.addoption('--python-path', action='store', help='Path to fileset.pyz')


@pytest.fixture(scope='session')
def fileset_path(pytestconfig):
    return pytestconfig.getoption('--fileset-path')
