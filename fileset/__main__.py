import coloredlogs

from fileset.cli import entrypoint as cli_entrypoint

coloredlogs.install(fmt='%(message)s')


def entrypoint():
    cli_entrypoint()


if __name__ == '__main__':
    entrypoint()
