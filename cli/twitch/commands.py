import click
from ..context import pass_config


@click.command()
@pass_config
def twitch(config):
    click.echo('this command is not implemented')
