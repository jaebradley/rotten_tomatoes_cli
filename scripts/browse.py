import click

from data.services import RottenTomatoesTvShowsBrowser
from tables.builders import BrowseTvShowTableBuilder
from data import BrowseTvShowCategory, BrowseMovieCategory


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


@click.command()
@click.argument("category", default=BrowseMovieCategory.opening["value"], type=click.Choice(BrowseMovieCategory.values()))
def movie(category):
    click.echo("movies")


browse.add_command(tv)
browse.add_command(movie)