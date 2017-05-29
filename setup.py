from setuptools import setup, find_packages

setup(
    name='rotten_tomatoes_cli',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'rotten_tomatoes_client==0.0.2',
        'terminaltables',
        'termcolor'
    ],
    entry_points={
        'console_scripts': [
            'rotten= scripts.rotten:rotten'
        ],
    }
)