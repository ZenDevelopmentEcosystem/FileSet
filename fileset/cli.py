import click


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(message='%(package)s, version %(version)s')
def entrypoint():
    pass
