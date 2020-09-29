import click
from ..context import pass_config
from .api import Twitch

# click.secho('Hello World!', fg='green')
# click.secho('Some more text', bg='blue', fg='white')
# click.secho('ATTENTION', blink=True, bold=True)


@click.group()
@pass_config
def twitch(_config):
    """
    Commands to fetch twitch info
    """
    pass


@twitch.command()
@pass_config
def top_streams(config):
    twitch = Twitch()
    auth_token = twitch.auth
    streams = twitch.top_streams(auth_token)
    for stream in streams:
        output = f'Streamer: {stream.user_name}\n'
        output += f'Game: {stream.game.name}\n'
        output += f'Viewers: {stream.viewer_count}\n'
        click.secho(output, fg='blue')


@twitch.command()
@pass_config
def creds(config):
    twitch = Twitch()
    click.echo(twitch.creds)


@twitch.command()
@pass_config
def auth_token(config):
    twitch = Twitch()
    click.echo(twitch.auth)
