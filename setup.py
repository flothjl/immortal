from setuptools import setup, find_packages

setup(
    name='yourpackage',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        myscript=cli.cli:entry_point
        myarg=cli_argparse.cli:entry_point
    ''',
)