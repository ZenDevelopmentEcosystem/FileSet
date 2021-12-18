import pytest
from implementation.fileset import *  # noqa: F403,F401
from implementation.package import *  # noqa: F403,F401
from implementation.pip import *  # noqa: F403,F401
from implementation.proc_check import *  # noqa: F403,F401
from implementation.timeout import *  # noqa: F403,F401
from infra import local  # noqa: F401
from run import run_shell  # noqa: F401


def pytest_addoption(parser):
    parser.addoption('--fileset-path', action='store', help='Path to fileset.pyz')
    parser.addoption('--sdist-package-path', action='store', help='Path to sdist package')
    parser.addoption('--wheel-package-path', action='store', help='Path to wheel package')


@pytest.fixture(scope='session')
def fileset_path(pytestconfig):
    return pytestconfig.getoption('--fileset-path')


@pytest.fixture(scope='session')
def sdist_package_path(pytestconfig):
    return pytestconfig.getoption('--sdist-package-path')


@pytest.fixture(scope='session')
def wheel_package_path(pytestconfig):
    return pytestconfig.getoption('--wheel-package-path')
