import logging
import os

import click
import coloredlogs

from fileset.config import get_config_path
from fileset.parsecfg import load_configuration

from .config import config_command
from .errorhandler import error_handler
from .store import create_store_command

UNIT_TEST_MODE = bool(os.getenv('UNIT_TEST_MODE', False))

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


entrypoint.add_command(config_command)

for store in configuration.stores.values():
    create_store_command(entrypoint, store)
