import os

from fileset.config import convert_cfg_path


def test_relative_path_gives_abs_path():
    result = convert_cfg_path('relative', '/cfg/file')
    assert result == '/cfg/relative'


def test_normalized_path():
    result = convert_cfg_path('../relative', '/cfg/file')
    assert result == '/relative'


def test_abs_gives_no_change():
    abspath = os.path.realpath('.')
    result = convert_cfg_path(abspath, 'cfg/file')
    assert result == abspath
