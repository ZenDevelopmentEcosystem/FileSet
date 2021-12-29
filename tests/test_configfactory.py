import pytest

from fileset.config import ConfigFactory
from fileset.exceptions import FileSetException

from .configutils import ObjectConfig, RawConfig, src_constructor


def assert_invalid_property(ctx, section):
    error = ctx.value
    assert isinstance(error, FileSetException)
    assert str(error) == f"Invalid property 'INVALID' in {section} definition"


def assert_missing_property(ctx, property, section):
    error = ctx.value
    assert isinstance(error, FileSetException)
    assert str(error) == f"Missing property '{property}' in {section} definition"


@pytest.fixture()
def raw():
    return RawConfig()


@pytest.fixture()
def expected():
    return ObjectConfig()


@pytest.fixture()
def cf():
    result = ConfigFactory()
    result.reg_src('src', src_constructor)
    return result


@pytest.fixture()
def invalid():
    return {'INVALID': 'path'}


@pytest.fixture()
def missing():
    return {}


def test_create_on_get(cf, raw, expected):
    result = cf.create_on_get(raw.on_get)
    assert result == expected.on_get


def test_create_on_get_invalid_property_raise_exception(cf, invalid):
    with pytest.raises(FileSetException) as ctx:
        cf.create_on_get(invalid)
    assert_invalid_property(ctx, 'on-get')


def test_create_on_get_missing_property_raise_exception(cf, missing):
    with pytest.raises(FileSetException) as ctx:
        cf.create_on_get(missing)
    assert_missing_property(ctx, 'run', 'on-get')


def test_create_cache(cf, raw, expected):
    result = cf.create_cache(raw.cache)
    assert result == expected.cache


def test_create_source(cf, raw, expected):
    result = cf.create_source('src', raw.source['src'])
    assert result == expected.source


def test_create_store(cf, raw, expected):
    result = cf.create_store('store', raw.store)
    assert result == expected.store


def test_create_stores(cf, raw, expected):
    result = cf.create_stores(raw.stores)
    assert result == expected.stores


def test_create_configuration(cf, raw, expected):
    result = cf.create_configuration(raw.configuration, 'config-file')
    assert result == expected.configuration


def test_create_configuration_missing_property_raise_exception(cf, missing):
    result = cf.create_configuration(missing, '')
    assert isinstance(result.error, FileSetException)
    assert str(result.error) == "Missing property 'file-stores' in root definition"
