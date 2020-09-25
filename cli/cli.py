import click
from .context import pass_config
from . import hello_world
from .twitch import commands as twitch
from .dotfiles import commands as dotfiles


@click.group()
@click.option('--verbose', '-v', is_flag=True)
@pass_config
def entry_point(_config, verbose):
    _config.verbose = verbose
    if verbose:
        click.echo('Running in verbose mode')


entry_point.add_command(hello_world.say)
entry_point.add_command(twitch.twitch)
entry_point.add_command(dotfiles.dotfiles)
