import click

from data import BrowseTvShowCategory
from data.services import RottenTomatoesTvShowsBrowser
from scripts.movies import movies
from tables.builders import BrowseTvShowTableBuilder


@click.group()
def browse():
    pass


@click.command()
@click.argument("category", default=BrowseTvShowCategory.new["value"], type=click.Choice(BrowseTvShowCategory.values()))
def tv(category):
    browser = RottenTomatoesTvShowsBrowser()
    results = browser.browse(category=BrowseTvShowCategory.category(value=category)["client_value"])
    browse_tv_show_table_builder = BrowseTvShowTableBuilder()
    if len(results) > 0:
        table = browse_tv_show_table_builder.build(tv_shows=results)
        click.echo(table)

browse.add_command(tv)
browse.add_command(movies)