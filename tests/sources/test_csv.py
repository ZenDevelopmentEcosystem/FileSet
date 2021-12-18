import pytest

from fileset.exceptions import FileSetException
from fileset.sources.csv import create


def test_create():
    result = create(
        {
            'file': 'index.csv',
            'id-column': 'id',
            'filename-column': 'filename',
            'filename-suffix': '.txt',
            'root-path': '/mnt/data'
        })
    assert result.file == 'index.csv'
    assert result.id_column == 'id'
    assert result.filename_column == 'filename'
    assert result.filename_suffix == '.txt'
    assert result.root_path == '/mnt/data'


def test_create_missing_property_raise_exception():

    with pytest.raises(FileSetException) as ctx:
        create(
            {
                # missing file
                'id-column': 'id',
                'filename-column': 'filename',
                'filename-suffix': '.txt',
                'root-path': '/mnt/data'
            })
    assert ctx.value.args[0] == "Missing property 'file' in csv definition"


def test_create_invalid_property_raise_exception():
    with pytest.raises(FileSetException) as ctx:
        create(
            {
                'file': 'index.csv',
                'id-column': 'id',
                'filename-column': 'filename',
                'filename-suffix': '.txt',
                'root-path': '/mnt/data',
                'INVALID': '',
            })
    assert ctx.value.args[0] == "Invalid property 'INVALID' in csv definition"
