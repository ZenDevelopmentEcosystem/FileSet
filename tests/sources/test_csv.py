import pytest

from fileset.exceptions import FileSetException
from fileset.sources.csv import CsvSource, constructor, representer

from ..configutils import CONFIG_PATH


@pytest.fixture()
def relraw():
    return {
        'index-file': 'index.csv',
        'id-column': 'id',
        'filename-column': 'filename',
        'filename-suffix': '.txt',
        'root-path': '../mnt/data'
    }


@pytest.fixture()
def relcsv():
    return CsvSource('index.csv', 'id', 'filename', '.txt', '../mnt/data')


@pytest.fixture()
def abscsv():
    return CsvSource('/cfg/index.csv', 'id', 'filename', '.txt', '/mnt/data')


@pytest.fixture()
def cfg_path():
    return CONFIG_PATH


def test_constructor(relraw, abscsv, cfg_path):
    result = constructor(relraw, cfg_path)
    assert isinstance(result, CsvSource)
    assert result == abscsv


def test_constructor_missing_property_raise_exception(relraw, cfg_path):
    del relraw['index-file']
    with pytest.raises(FileSetException) as ctx:
        constructor(relraw, cfg_path)
    assert ctx.value.args[0] == "Missing property 'index-file' in csv definition"


def test_constructor_invalid_property_raise_exception(relraw, cfg_path):
    relraw['INVALID'] = ''
    with pytest.raises(FileSetException) as ctx:
        constructor(relraw, cfg_path)
    assert ctx.value.args[0] == "Invalid property 'INVALID' in csv definition"


def test_representer(relcsv, relraw):
    result = representer(relcsv)
    expected = {'csv': relraw}
    assert result == expected
