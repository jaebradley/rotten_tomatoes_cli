import click

from scripts.browse import browse
from scripts.search import search


@click.group()
def rotten():
    pass

rotten.add_command(browse)
rotten.add_command(search)
