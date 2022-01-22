import coloredlogs

from fileset.cli.main import entrypoint

coloredlogs.install(fmt='%(message)s')

if __name__ == '__main__':
    entrypoint()
