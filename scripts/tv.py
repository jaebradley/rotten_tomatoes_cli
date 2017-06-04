import click

from data import BrowseTvShowCategory
from data.services import RottenTomatoesTvShowsBrowser
from tables.builders import BrowseTvShowTableBuilder
from tables.rows.builders import BrowseTvShowRowBuilder

browser = RottenTomatoesTvShowsBrowser()
browse_tv_show_table_builder = BrowseTvShowTableBuilder(BrowseTvShowRowBuilder())


@click.command()
@click.argument("category", default=BrowseTvShowCategory.new.name, type=click.Choice(BrowseTvShowCategory.names()))
def tv(category):
    tv_shows = browser.browse(category=BrowseTvShowCategory.category(value=category).value["client_category"])
    if len(tv_shows) > 0:
        table = browse_tv_show_table_builder.build(tv_shows)
        click.echo(table)
