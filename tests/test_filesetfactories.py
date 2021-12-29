import pytest

from fileset.exceptions import FileSetException
from fileset.sets import FileSet, FileSetFactory, RawFactory


@pytest.fixture()
def raw():
    return {'sets': {'s1': {'s2': ['a1', 'a2']}}}


@pytest.fixture()
def fs():
    s1 = FileSet('s1')
    s2 = FileSet('s2')
    s2.add_assets(['a1', 'a2'])
    s1.add_set(s2)
    return s1


@pytest.fixture()
def invalid():
    return {'sets': {'s1': 'scalar'}}


@pytest.fixture()
def fsf():
    return FileSetFactory()


@pytest.fixture()
def rf():
    return RawFactory()


def test_filesetfactory_create(fsf, raw):
    fs, = fsf.create_filesets(raw['sets'])
    assert fs.name == 's1'
    assert fs.sets[0].name == 's2'
    assert fs.sets[0].assets == ['a1', 'a2']


def test_filesetfactory_create_invalid_structure(fsf, invalid):
    with pytest.raises(FileSetException) as ctx:
        fsf.create_filesets(invalid)
    error = ctx.value
    assert isinstance(error, FileSetException)
    assert str(error) == "Unknown subsection type <class 'str'> for s1"


def test_rawfactory_create(rf, fs, raw):
    result = rf.create_filesets([fs])
    assert result == raw
