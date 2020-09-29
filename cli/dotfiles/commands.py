import click
import yaml
from ..context import pass_config
from .exceptions import UnsupportedDotfileType
from .zsh import process_zsh
import os

SUPPORTED_DOTFILE_TYPES = ['generic', 'zsh']


@click.group()
@pass_config
def dotfiles(_config):
    """
    Commands to deal with dotfile maintenence
    """
    pass


@dotfiles.command()
@click.option('--file', help='path to yaml file')
@pass_config
def install(_config, file):
    """
    Install dotfile
    """
    if _config.verbose:
        click.echo(f'reading file from : {file}')

    with open(file) as yaml_file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        documents = yaml.full_load(yaml_file)
        config = documents
        if _config.verbose:
            click.echo(config)
        for item in config:
            if item['type'] not in SUPPORTED_DOTFILE_TYPES:
                raise click.ClickException(
                    f'{item["type"]} is not currently a supported dotfile type')
            if item['type'] == 'zsh':
                process_zsh(item)
            for file_ in item.get('files', []):
                if os.path.exists(file_['path']):
                    os.remove(file_['path'])
                os.system(f'cp {file_["path"]} {file_["destination"]}')
    click.secho('🤩🤩INSTALLATION SUCCESSFUL🤩🤩')
