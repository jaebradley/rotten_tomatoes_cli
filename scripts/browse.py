import click

from scripts.movies import movies
from scripts.tv import tv


@click.group()
def browse():
    pass


browse.add_command(tv)
browse.add_command(movies)