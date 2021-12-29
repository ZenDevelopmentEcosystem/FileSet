from collections import namedtuple

from fileset.config import get_config_factory, get_raw_factory, missing_property_handler, \
    validate_properties

CSV_PROPERTIES = ['index-file', 'id-column', 'filename-column', 'filename-suffix', 'root-path']
CSV_SOURCE_NAME = 'csv'

CsvSource = namedtuple('CsvSource', 'index_file, id_column, filename_column, filename_suffix, root_path')


def constructor(raw_config):
    validate_properties(raw_config, CSV_PROPERTIES, CSV_SOURCE_NAME)
    return missing_property_handler(
        lambda: CsvSource(
            raw_config['index-file'], raw_config['id-column'], raw_config['filename-column'], raw_config[
                'filename-suffix'], raw_config['root-path']), CSV_SOURCE_NAME)


def representer(csv):
    return {
        CSV_SOURCE_NAME: {
            'index-file': csv.index_file,
            'id-column': csv.id_column,
            'filename-column': csv.filename_column,
            'filename-suffix': csv.filename_suffix,
            'root-path': csv.root_path
        }
    }


get_config_factory().reg_src(CSV_SOURCE_NAME, constructor)

get_raw_factory().reg_src(CsvSource, representer)
