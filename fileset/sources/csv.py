from fileset.config import get_config_factory, missing_property_handler, validate_properties

CSV_PROPERTIES = ['file', 'id-column', 'filename-column', 'filename-suffix', 'root-path']


class CsvSource:

    def __init__(self, file, id_column, filename_column, filename_suffix, root_path):
        self.file = file
        self.id_column = id_column
        self.filename_column = filename_column
        self.filename_suffix = filename_suffix
        self.root_path = root_path


def create(raw_config):
    validate_properties(raw_config, CSV_PROPERTIES, 'csv')
    return missing_property_handler(
        lambda: CsvSource(
            raw_config['file'], raw_config['id-column'], raw_config['filename-column'], raw_config['filename-suffix'],
            raw_config['root-path']), 'csv')


get_config_factory().reg_src('csv', create)
