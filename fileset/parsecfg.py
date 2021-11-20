from os import environ
from pathlib import Path

from ruamel.yaml import YAML

import fileset.storageengines.csv  # noqa disable=F401

from .config import get_config_factory
from .exception import FileSetException

CONFIG_FILE = Path(environ.get('FILESET_CONFIG', '~/.fileset.yml')).expanduser().absolute()


def get_yaml_data(self, config_path):
    yaml = YAML(typ='rt')
    try:
        with open(config_path) as f:
            return yaml.load(f)
    except Exception as e:
        msg = f'Failed to load config due to error: {str(e)}'
        raise FileSetException(msg)


def get_stores(config_file):
    cf = get_config_factory()
    raw_config = get_yaml_data(config_file)
    return cf.create_stores(raw_config['file-stores'])
