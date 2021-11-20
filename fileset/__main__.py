import click
import coloredlogs

coloredlogs.install(fmt='%(message)s')


@click.group(context_settings={'help_option_names': ['-h', '--help']})
def entrypoint() -> None:
    pass


if __name__ == '__main__':
    entrypoint()
