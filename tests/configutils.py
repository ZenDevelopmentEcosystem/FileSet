from collections import namedtuple

from fileset.config import Cache, Configuration, OnGet, Store

DummySource = namedtuple('DummySource', 'property')


def src_constructor(raw_config):
    return DummySource(raw_config['property'])


def src_representer(dummy_src):
    return {'src': {'property': dummy_src.property}}


class RawConfig:

    def __init__(self):
        self.on_get = {'run': 'cmd'}
        self.source = {'src': {'property': 'value'}}
        self.cache = {'path': 'cache-path'}
        self.store = {
            'source': self.source,
            'cache': self.cache,
            'on-get': self.on_get,
        }
        self.stores = {
            'store1': self.store,
            'store2': self.store,
        }
        self.configuration = {'file-stores': self.stores}


class ObjectConfig:

    def __init__(self):
        self.on_get = OnGet('cmd')
        self.source = DummySource('value')
        self.cache = Cache('cache-path')
        self.store = Store('store', self.source, self.cache, self.on_get)
        self.stores = {
            'store1': Store('store1', self.source, self.cache, self.on_get),
            'store2': Store('store2', self.source, self.cache, self.on_get),
        }
        self.configuration = Configuration('config-file')
        self.configuration.stores = self.stores
