import logging
import sys

from fileset.exceptions import FileSetException

from .exitcodes import EXIT_CODE_GENERAL_ERROR, EXIT_CODE_GENERAL_FILESET_ERROR

logger = logging.getLogger()


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
