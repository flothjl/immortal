import click
import yaml
from ..context import pass_config
from .exceptions import UnsupportedDotfileType
import os

SUPPORTED_DOTFILE_TYPES = ['zsh']


@click.group()
@click.option('--repeat', help='How many times to greet you')
@pass_config
def dotfiles(_config, repeat):
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
                click.echo('Preparing your zsh dotfiles')
                if item.get('install-file'):
                    click.echo('Install File Provided')
                    install_path = os.path.join(
                        item.get('base-path', ''), f'{item.get("name","")}/{item.get("install-file")}')
                    with open(install_path, 'r') as install:
                        script = install.read()
                        install_output = os.system(script)
                for theme in item.get('themes', []):
                    click.echo(f'Installing a theme.')
                    install_path = os.path.join(
                        item.get(
                            'base-path', ''), f'{item.get("name","")}/{theme.get("install-file")}'
                    )
                    with open(install_path, 'r') as install:
                        script = install.read()
                        install_output = os.system(script)
            click.echo('Installation complete. Copying dotfiles.')
            for file_ in item.get('files', []):
                if os.path.exists(file_['path']):
                    os.remove(file_['path'])
                os.system(f'cp {file_["path"]} {file_["destination"]}')
