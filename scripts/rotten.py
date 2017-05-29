import click

from scripts.browse import browse


@click.group()
def rotten():
    pass

rotten.add_command(browse)
