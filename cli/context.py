import click
import os
import pathlib


class Config:
    def __init__(self):
        self.verbose = False
        self.root_path = pathlib.Path(__file__).parent.absolute()


pass_config = click.make_pass_decorator(Config, ensure=True)
