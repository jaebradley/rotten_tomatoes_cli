from setuptools import setup, find_packages

setup(
    name='rotten_tomatoes_cli',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'rotten_tomatoes_client',
        'emoji',
        'terminaltables',
        'termcolor'
    ],
    entry_points={
        'console_scripts': [
            'search = scripts.search:search'
        ],
    }
)