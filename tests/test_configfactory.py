import pytest

from fileset.config import Cache, ConfigFactory, OnGet, Store
from fileset.exceptions import FileSetException


class DummySource:

    def __init__(self, property):
        self.property = property


def src_constructor(raw_config):
    return DummySource(raw_config['property'])


class RawConfig:

    def __init__(self):
        self.on_get = {'run': 'cmd'}
        self.source = {'property': 'value'}
        self.cache = {'path': 'cache-path'}
        self.store = {
            'source': {
                'src': self.source,
            },
            'cache': self.cache,
            'on-get': self.on_get,
        }
        self.stores = {
            'store1': self.store,
            'store2': self.store,
        }


class ExpectedConfig:

    def __init__(self):
        self.on_get = OnGet('cmd')
        self.source = DummySource('value')
        self.cache = Cache('cache-path')
        self.store = Store('store', self.source, self.cache, self.on_get)
        self.stores = {
            'store1': Store('store1', self.source, self.cache, self.on_get),
            'store2': Store('store2', self.source, self.cache, self.on_get),
        }


class CheckConfig:

    def on_get(self, expected, result):
        assert expected.run == result.run

    def cache(self, expected, result):
        assert expected.path == result.path

    def source(self, expected, result):
        assert expected.property == result.property

    def store(self, expected, result):
        assert expected.name == result.name
        self.on_get(expected.on_get, result.on_get)
        self.cache(expected.cache, result.cache)
        self.source(expected.source, result.source)

    def stores(self, expected, result):
        for store in list(expected):
            self.store(expected[store], result[store])


def assert_invalid_property(ctx, section):
    assert ctx.value.args[0] == f"Invalid property 'INVALID' in {section} definition"


def assert_missing_property(ctx, property, section):
    assert ctx.value.args[0] == f"Missing property '{property}' in {section} definition"


@pytest.fixture()
def raw():
    return RawConfig()


@pytest.fixture()
def expected():
    return ExpectedConfig()


@pytest.fixture()
def cf():
    result = ConfigFactory()
    result.reg_src('src', src_constructor)
    return result


@pytest.fixture()
def check():
    return CheckConfig()


@pytest.fixture()
def invalid():
    return {'INVALID': 'path'}


@pytest.fixture()
def missing():
    return {}


# -- on_get --


def test_create_on_get(cf, raw, expected, check):
    result = cf.create_on_get(raw.on_get)
    check.on_get(expected.on_get, result)


def test_create_on_get_invalid_property_raise_exception(cf, invalid):
    with pytest.raises(FileSetException) as ctx:
        cf.create_on_get(invalid)
    assert_invalid_property(ctx, 'on-get')


def test_create_on_get_missing_property_raise_exception(cf, missing):
    with pytest.raises(FileSetException) as ctx:
        cf.create_on_get(missing)
    assert_missing_property(ctx, 'run', 'on-get')


def test_create_cache(cf, raw, expected, check):
    result = cf.create_cache(raw.cache)
    check.cache(expected.cache, result)


def test_create_source(cf, raw, expected, check):
    result = cf.create_source('src', raw.source)
    check.source(expected.source, result)


def test_create_store(cf, raw, expected, check):
    result = cf.create_store('store', raw.store)
    check.store(expected.store, result)


def test_create_stores(cf, raw, expected, check):
    result = cf.create_stores(raw.stores)
    check.stores(expected.stores, result)
