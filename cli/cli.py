import click
from .context import pass_config
from . import hello_world



@click.group()
@click.option('--verbose','-v', is_flag=True)
@pass_config
def entry_point(config, verbose):
    config.verbose = verbose
    if verbose:
        click.echo('Running in verbose mode')

entry_point.add_command(hello_world.say)
