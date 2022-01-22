from .config import pass_configuration
from .errorhandler import error_handler


def create_store_command(main_command, store):

    @main_command.command(name=store.name, short_help=f'Operate on file store {store.name}')
    @pass_configuration
    @error_handler
    def store_command(configuration):
        print(f'store={store.name}')
