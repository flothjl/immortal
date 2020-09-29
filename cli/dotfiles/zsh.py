import click
import os


def process_zsh(item: dict):
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
