import pytest

from fileset.exceptions import FileSetException
from fileset.sources.csv import CsvSource, constructor, representer


def get_raw():
    return {
        'index-file': 'index.csv',
        'id-column': 'id',
        'filename-column': 'filename',
        'filename-suffix': '.txt',
        'root-path': '/mnt/data'
    }


def get_csv():
    return CsvSource('index.csv', 'id', 'filename', '.txt', '/mnt/data')


def test_constructor():
    result = constructor(get_raw())
    expected = get_csv()
    assert isinstance(result, CsvSource)
    assert result == expected


def test_constructor_missing_property_raise_exception():
    raw = get_raw()
    del raw['index-file']
    with pytest.raises(FileSetException) as ctx:
        constructor(raw)
    assert ctx.value.args[0] == "Missing property 'index-file' in csv definition"


def test_constructor_invalid_property_raise_exception():
    raw = get_raw()
    raw['INVALID'] = ''
    with pytest.raises(FileSetException) as ctx:
        constructor(raw)
    assert ctx.value.args[0] == "Invalid property 'INVALID' in csv definition"


def test_representer():
    result = representer(get_csv())
    expected = {'csv': get_raw()}
    assert result == expected
