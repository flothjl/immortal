import click
from .context import pass_config

@click.command()
@click.option('--name', default='World', help='The name to greet')
@click.option('--repeat', default=1, help='How many times to greet you')
@click.argument('out',type=click.File('w'), default='-', required=False)
@pass_config
def say(config, name, repeat, out):
    """
    This script greets you
    """
    if config.verbose:
        click.echo(f'Processing your request.\nInput: {name}\nRepeat:{repeat}')
    for i in range(repeat):
        click.echo(f'Hello, {name}', file=out)