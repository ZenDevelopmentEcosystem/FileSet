from fileset.exceptions import FileSetException

STORE_PROPERTIES = ['source', 'cache', 'on-get']
SOURCE_PROPERTIES = []
CACHE_PROPERTIES = ['path']
ON_GET_PROPERTIES = ['run']


def validate_properties(raw_config, valid_properties, section):
    for prop in list(raw_config):
        if prop not in valid_properties:
            raise FileSetException(f"Invalid property '{prop}' in {section} definition")


def missing_property_handler(func, section):
    try:
        return func()
    except KeyError as err:
        raise FileSetException(f'Missing property {err} in {section} definition')


class ConfigFactory:

    def __init__(self):
        self.src_constructors = {}

    def create_stores(self, raw_config):
        result = {}
        for store in list(raw_config):
            result[store] = self.create_store(store, raw_config[store])
        return result

    def create_store(self, name, raw_config):
        source_type = list(raw_config['source'])[0]
        source_raw = raw_config['source'][source_type]
        return Store(
            name, self.create_source(source_type, source_raw), self.create_cache(raw_config['cache']),
            self.create_on_get(raw_config['on-get']))

    def create_cache(self, raw_config):
        return Cache(raw_config['path'])

    def create_on_get(self, raw_config):
        validate_properties(raw_config, ON_GET_PROPERTIES, 'on-get')
        return missing_property_handler(lambda: OnGet(raw_config['run']), 'on-get')

    def create_source(self, name, raw_config):
        return self.src_constructors[name](raw_config)

    def reg_src(self, name, constructor):
        self.src_constructors[name] = constructor


class Store:

    def __init__(self, name, source, cache, on_get):
        self.name = name
        self.source = source
        self.cache = cache
        self.on_get = on_get


class Cache:

    def __init__(self, path):
        self.path = path


class OnEvent:

    def __init__(self, run):
        self.run = run


class OnGet(OnEvent):
    pass


CONFIG_FACTORY = ConfigFactory()


def get_config_factory():
    return CONFIG_FACTORY
