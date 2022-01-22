import logging
import os
import sys

import click

from fileset.config import Configuration

from .errorhandler import error_handler
from .exitcodes import EXIT_CODE_FAILED_CONFIG_VALIDATION

pass_configuration = click.make_pass_decorator(Configuration)


@click.command(name='config', short_help='Validate and print configuration.')
@click.option('--quiet', '-q', 'quiet', default=False, flag_value=True, help='Silence output - except errors.')
@click.option(
    '--set-file', 'print_set_filename', default=False, flag_value=True, help='Print set filename only - no validation.')
@click.option(
    '--config-file',
    'print_config_filename',
    default=False,
    flag_value=True,
    help='Print config filename only - no validation.')
@click.option('--set', '-s', 'set_file', type=click.Path(), default='FileSet.yml', help='set-file')
@click.option('--set-paths', 'print_set_paths', default=False, flag_value=True, help="Print sets' paths.")
@click.option('--asset-paths', 'print_asset_paths', default=False, flag_value=True, help="Print assets' paths.")
@pass_configuration
@error_handler
def config_command(
        configuration, quiet, print_set_filename, print_config_filename, set_file, print_set_paths, print_asset_paths):
    """Validate and print configuration."""
    from fileset.parsecfg import config_to_yaml, load_set_file, sets_to_yaml
    from fileset.sets import print_assets_as_paths, print_sets_as_paths

    stream = sys.stdout
    set_file = os.path.abspath(set_file)
    filesets = load_set_file(set_file)

    if print_config_filename:
        print(configuration.config_file, file=stream)
        return

    if print_set_filename:
        print(set_file, file=stream)
        return

    if print_set_paths:
        print_sets_as_paths(filesets, sys.stdout)
        return

    if print_asset_paths:
        print_assets_as_paths(filesets, sys.stdout)
        return

    if not quiet:
        config_to_yaml(configuration, sys.stdout)

    if not quiet:
        sets_to_yaml(filesets, sys.stdout)

    if configuration.error is not None:
        logging.error(str(configuration.error))
        sys.exit(EXIT_CODE_FAILED_CONFIG_VALIDATION)
