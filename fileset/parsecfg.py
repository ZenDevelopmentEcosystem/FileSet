import os

from ruamel.yaml import YAML

import fileset.sources.csv  # noqa disable=F401

from .config import Configuration, get_config_factory, get_raw_factory, missing_property_handler, \
    validate_properties
from .exceptions import FileSetException
from .sets import SETS_PROPERTIES, FileSetFactory
from .sets import RawFactory as RawFileSetFactory


def get_yaml_data(config_path):
    yaml = YAML(typ='rt')
    try:
        with open(config_path) as f:
            return yaml.load(f)
    except Exception as e:
        msg = f"Failed to load settings from file '{config_path}' due to error: {str(e)}"
        raise FileSetException(msg)


def write_yaml_data(data, stream):
    yaml = YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.dump(data, stream)


def load_configuration(config_file):
    cfg = None
    try:
        raw_config = get_yaml_data(config_file)
        cf = get_config_factory()
        cfg = cf.create_configuration(raw_config, config_file)
    except Exception as e:
        cfg = Configuration(config_file)
        cfg.error = e
    return cfg


def config_to_yaml(configuration, stream):
    rf = get_raw_factory()
    raw = rf.create_configuration(configuration)
    write_yaml_data(raw, stream)


def load_set_file(set_file):
    if not os.path.exists(set_file):
        return []
    raw = get_yaml_data(set_file)
    validate_properties(raw, SETS_PROPERTIES, 'root')
    fsf = FileSetFactory()
    return missing_property_handler(lambda: fsf.create_filesets(raw['sets']), 'root')


def sets_to_yaml(filesets, stream):
    rf = RawFileSetFactory()
    raw = rf.create_filesets(filesets)
    write_yaml_data(raw, stream)
