import logging
import os
from collections import namedtuple

from fileset.exceptions import FileSetException

CONFIGURATION_ENVIRONMENTAL_VARIABLE = 'FILESET_CONFIG'
CONFIGURATION_PROPERTIES = ['file-stores']
STORE_PROPERTIES = ['source', 'cache', 'on-get']
SOURCE_PROPERTIES = []
CACHE_PROPERTIES = ['path']
ON_GET_PROPERTIES = ['run']

Store = namedtuple('Store', 'name, source, cache, on_get')
Cache = namedtuple('Cache', 'path')
OnGet = namedtuple('OnGet', 'run')


def validate_properties(raw_config, valid_properties, section):
    for prop in list(raw_config):
        if prop not in valid_properties:
            raise FileSetException(f"Invalid property '{prop}' in {section} definition")


def missing_property_handler(func, section):
    try:
        return func()
    except KeyError as err:
        raise FileSetException(f'Missing property {err} in {section} definition')


def convert_cfg_path(path, config_file):
    if not os.path.isabs(path):
        config_dir = os.path.dirname(config_file)
        path = os.path.abspath(os.path.join(config_dir, path))
    return path


class ConfigFactory:

    def __init__(self):
        self.src_constructors = {}

    def reg_src(self, name, constructor):
        self.src_constructors[name] = constructor

    def create_configuration(self, raw_config, config_file):
        cfg = Configuration(config_file)
        try:
            validate_properties(raw_config, CONFIGURATION_PROPERTIES, 'root')
            cfg.stores = missing_property_handler(
                lambda: self.create_stores(raw_config['file-stores'], config_file), 'root')
        except Exception as err:
            logging.error(f'Could not create configuration, error: {err}')
            cfg.error = err
        return cfg

    def create_stores(self, raw_config, config_file):
        return {name: self.create_store(name, raw_store, config_file) for name, raw_store in raw_config.items()}

    def create_store(self, name, raw_config, config_file):
        source_type = list(raw_config['source'])[0]
        source_raw = raw_config['source'][source_type]
        return Store(
            name, self.create_source(source_type, source_raw, config_file),
            self.create_cache(raw_config['cache'], config_file), self.create_on_get(raw_config['on-get']))

    def create_cache(self, raw_config, config_file):
        validate_properties(raw_config, CACHE_PROPERTIES, 'cache')
        return missing_property_handler(lambda: Cache(convert_cfg_path(raw_config['path'], config_file)), 'cache')

    def create_on_get(self, raw_config):
        validate_properties(raw_config, ON_GET_PROPERTIES, 'on-get')
        return missing_property_handler(lambda: OnGet(raw_config['run']), 'on-get')

    def create_source(self, name, raw_config, config_file):
        return self.src_constructors[name](raw_config, config_file)


class RawFactory:

    def __init__(self):
        self.src_representers = {}

    def reg_src(self, cls, representer):
        self.src_representers[cls] = representer

    def create_configuration(self, configuration):
        return {'file-stores': self.create_stores(configuration.stores)}

    def create_stores(self, stores):
        return {name: self.create_store(store) for name, store in stores.items()}

    def create_store(self, store):
        return {
            'source': self.create_source(store.source),
            'cache': self.create_cache(store.cache),
            'on-get': self.create_on_get(store.on_get)
        }

    def create_cache(self, cache):
        return {'path': cache.path}

    def create_on_get(self, on_get):
        return {'run': on_get.run}

    def create_source(self, source):
        return self.src_representers[type(source)](source)


class Configuration():

    def __init__(self, config_file):
        self.config_file = config_file
        self.stores = {}
        self.runs = {}
        self.error = None

    def __eq__(self, other):
        return isinstance(other, type(self)) \
            and self.config_file == other.config_file \
            and self.stores == other.stores \
            and self.runs == other.runs \
            and self.error == other.error


CONFIG_FACTORY = ConfigFactory()
RAW_FACTORY = RawFactory()


def get_config_factory():
    return CONFIG_FACTORY


def get_raw_factory():
    return RAW_FACTORY


def get_config_path():
    return os.path.abspath(os.environ.get(CONFIGURATION_ENVIRONMENTAL_VARIABLE, os.path.expanduser('~/.fileset.yml')))
