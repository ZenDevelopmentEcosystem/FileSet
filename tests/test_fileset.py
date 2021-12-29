import pytest

from fileset.sets import FileSet


@pytest.fixture(name='fs')
def get_fileset():
    s1 = FileSet('s1')
    s1.add_asset('a1')
    s2 = FileSet('s2')
    s2.add_asset('a1')
    s2.add_asset('a2')
    s1.add_set(s2)
    return s1


def test_add_asset():
    fs = FileSet('fs')
    fs.add_asset('a1')
    assert fs.assets == ['a1']


def test_add_assets():
    fs = FileSet('fs')
    assets = ['a1', 'a2']
    fs.add_assets(assets)
    assert fs.assets == assets


def test_add_set():
    fs = FileSet('fs')
    subset = FileSet('sub')
    fs.add_set(subset)
    assert fs.sets == [subset]


def test_add_sets():
    fs = FileSet('fs')
    subsets = [FileSet('sub1'), FileSet('sub2')]
    fs.add_sets(subsets)
    assert fs.sets == subsets


def test_all_assets(fs):
    assert fs.all_assets == ['a1', 'a2']


def test_all_sets(fs):
    assert fs.all_sets == [fs, *fs.sets]
