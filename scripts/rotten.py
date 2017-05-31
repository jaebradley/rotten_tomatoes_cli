import click

from scripts.movies import movies
from scripts.search import search
from scripts.tv import tv


@click.group()
def rotten():
    pass

rotten.add_command(movies)
rotten.add_command(tv)
rotten.add_command(search)
