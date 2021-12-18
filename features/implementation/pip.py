import os

import pytest
from pytest_bdd import parsers, then


@pytest.fixture()
def pip_path(venv_dir):
    return os.path.join(venv_dir, 'bin', 'pip')


@then(parsers.parse('pip package `{package}` is installed'))
def pip_package_is_installed(package, local, pip_path):
    assert local.pip(package, pip_path=pip_path).is_installed
