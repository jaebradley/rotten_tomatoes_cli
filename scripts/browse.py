import click

from data import BrowseTvShowCategory
from data.services import RottenTomatoesTvShowsBrowser
from scripts.movies import movies
from tables.builders import BrowseTvShowTableBuilder


@click.group()
def browse():
    pass


@click.command()
@click.argument("category", default=BrowseTvShowCategory.new.name, type=click.Choice(BrowseTvShowCategory.names()))
def tv(category):
    browser = RottenTomatoesTvShowsBrowser()
    results = browser.browse(category=BrowseTvShowCategory.category(value=category)[0]["client_category"])
    browse_tv_show_table_builder = BrowseTvShowTableBuilder()
    if len(results) > 0:
        table = browse_tv_show_table_builder.build(tv_shows=results)
        click.echo(table)

browse.add_command(tv)
browse.add_command(movies)