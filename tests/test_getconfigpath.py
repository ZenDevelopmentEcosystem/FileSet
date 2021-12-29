import os

import pytest

from fileset.config import CONFIGURATION_ENVIRONMENTAL_VARIABLE, get_config_path

CONFIG_FILE_PATH = '/abspath/config-file'


@pytest.fixture()
def set_env():
    original = os.environ.get(CONFIGURATION_ENVIRONMENTAL_VARIABLE, None)
    os.environ[CONFIGURATION_ENVIRONMENTAL_VARIABLE] = CONFIG_FILE_PATH
    yield
    if original is None:
        del os.environ[CONFIGURATION_ENVIRONMENTAL_VARIABLE]
    else:
        os.environ[CONFIGURATION_ENVIRONMENTAL_VARIABLE] = original


@pytest.fixture()
def unset_env():
    original = os.environ.get(CONFIGURATION_ENVIRONMENTAL_VARIABLE, None)
    os.environ.pop(CONFIGURATION_ENVIRONMENTAL_VARIABLE, None)
    yield
    if original is not None:
        os.environ[CONFIGURATION_ENVIRONMENTAL_VARIABLE] = original


def test_get_config_path_with_envvar(set_env):
    result = get_config_path()
    assert result == CONFIG_FILE_PATH


def test_get_config_path_with_default(unset_env):
    result = get_config_path()
    assert '/home' in result
