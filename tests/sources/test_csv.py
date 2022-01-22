import pytest

from fileset.exceptions import FileSetException
from fileset.sources.csv import CsvSource, constructor, representer

@pytest.fixture(name='raw')
def get_raw():
    return {
        'index-file': 'index.csv',
        'id-column': 'id',
        'filename-column': 'filename',
        'filename-suffix': '.txt',
        'root-path': '/mnt/data'
    }

@pytest.fixture(name='csv')
def get_csv():
    return CsvSource('index.csv', 'id', 'filename', '.txt', '/mnt/data')


def test_constructor(raw, csv):
    result = constructor(raw)
    assert isinstance(result, CsvSource)
    assert result == csv


def test_constructor_missing_property_raise_exception(raw):
    del raw['index-file']
    with pytest.raises(FileSetException) as ctx:
        constructor(raw)
    assert ctx.value.args[0] == "Missing property 'index-file' in csv definition"


def test_constructor_invalid_property_raise_exception(raw):
    raw['INVALID'] = ''
    with pytest.raises(FileSetException) as ctx:
        constructor(raw)
    assert ctx.value.args[0] == "Invalid property 'INVALID' in csv definition"


def test_representer(csv, raw):
    result = representer(csv)
    expected = {'csv': raw}
    assert result == expected
