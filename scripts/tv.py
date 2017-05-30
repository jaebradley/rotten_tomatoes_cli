import click

from data import BrowseTvShowCategory
from data.services import RottenTomatoesTvShowsBrowser
from tables.builders import BrowseTvShowTableBuilder


@click.command()
@click.argument("category", default=BrowseTvShowCategory.new.name, type=click.Choice(BrowseTvShowCategory.names()))
def tv(category):
    browser = RottenTomatoesTvShowsBrowser()
    results = browser.browse(category=BrowseTvShowCategory.category(value=category).value["client_category"])
    browse_tv_show_table_builder = BrowseTvShowTableBuilder()
    if len(results) > 0:
        table = browse_tv_show_table_builder.build(tv_shows=results)
        click.echo(table)
