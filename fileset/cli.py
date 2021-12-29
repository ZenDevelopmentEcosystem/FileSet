import logging
import os
import sys

import click
import coloredlogs

from .config import Configuration, get_config_path
from .exceptions import FileSetException
from .parsecfg import config_to_yaml, load_configuration, load_set_file, sets_to_yaml
from .sets import print_assets_as_paths, print_sets_as_paths

EXIT_CODE_GENERAL_ERROR = 8
EXIT_CODE_GENERAL_FILESET_ERROR = 9
EXIT_CODE_FAILED_CONFIG_VALIDATION = 10

UNIT_TEST_MODE = bool(os.getenv('UNIT_TEST_MODE', False))

pass_configuration = click.make_pass_decorator(Configuration)
logger = logging.getLogger()
configuration = load_configuration(get_config_path())


def get_loglevel_from_verbosity(verbosity):
    if verbosity >= 3:
        return logging.DEBUG
    elif verbosity >= 2:
        return logging.INFO
    elif verbosity >= 1:
        return logging.WARNING
    elif verbosity >= 0:
        return logging.CRITICAL


def error_handler(f):
    if not callable(f):
        raise FileSetException('Must be called without arguments')

    def decorator(*argv, **kwargs):
        try:
            f(*argv, **kwargs)
        except FileSetException as e:
            logger.critical(str(e))
            sys.exit(EXIT_CODE_GENERAL_FILESET_ERROR)
        except Exception as e:
            logger.exception(str(e))
            sys.exit(EXIT_CODE_GENERAL_ERROR)

    return decorator


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(message='%(package)s, version %(version)s')
@click.option('--verbose', '-v', 'verbosity', count=True, default=0, help='More verbose output. Multiple is allowed.')
@click.pass_context
@error_handler
def entrypoint(ctx, verbosity):
    """Commandline tool for syncing and running commands on file sets."""
    ctx.obj = configuration
    logger.setLevel(logging.DEBUG)
    if UNIT_TEST_MODE:
        logger.setLevel(get_loglevel_from_verbosity(verbosity))
    else:
        coloredlogs.install(fmt='%(message)s', logger=logger, level=get_loglevel_from_verbosity(verbosity))


@entrypoint.command(name='config', short_help='Validate and print configuration.')
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


def create_store_command(store):

    @entrypoint.command(name=store.name, short_help=f'Operate on file store {store.name}')
    @pass_configuration
    @error_handler
    def store_command(configuration):
        print(f'store={store.name}')


for store in configuration.stores.values():
    create_store_command(store)
