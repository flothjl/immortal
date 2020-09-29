from setuptools import setup, find_packages

setup(
    name='immortal',
    author='J. Floth',
    version='0.1',
    url='https://github.com/flothjl/immortal',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        immortal=cli.cli:entry_point
        myarg=cli_argparse.cli:entry_point
    ''',
)
