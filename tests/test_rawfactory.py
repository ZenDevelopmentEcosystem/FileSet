import pytest

from fileset.config import RawFactory

from .configutils import DummySource, RelObjectConfig, RelRawConfig, src_representer


@pytest.fixture()
def expected():
    return RelRawConfig()


@pytest.fixture()
def cfg():
    return RelObjectConfig()


@pytest.fixture()
def rf():
    result = RawFactory()
    result.reg_src(DummySource, src_representer)
    return result


def test_create_on_get(rf, cfg, expected):
    result = rf.create_on_get(cfg.on_get)
    assert result == expected.on_get


def test_create_cache(rf, cfg, expected):
    result = rf.create_cache(cfg.cache)
    assert result == expected.cache


def test_create_source(rf, cfg, expected):
    result = rf.create_source(cfg.source)
    assert result == expected.source


def test_create_store(rf, cfg, expected):
    result = rf.create_store(cfg.store)
    assert result == expected.store


def test_create_stores(rf, cfg, expected):
    result = rf.create_stores(cfg.stores)
    assert result == expected.stores


def test_create_configuration(rf, cfg, expected):
    result = rf.create_configuration(cfg.configuration)
    assert result == expected.configuration
