import click

from data.services import RottenTomatoesTvShowsBrowser
from tables.builders import BrowseTvShowTableBuilder
from rotten_tomatoes_client import TvBrowsingCategory


@click.group()
def browse():
    pass


@click.command()
@click.argument("category", default="new_tonight", type=click.Choice(["new_tonight", "most_popular", "certified_fresh"]))
def tv(category):
    browser = RottenTomatoesTvShowsBrowser()
    results = browser.browse(category=TvBrowsingCategory.new_tv_tonight)
    browse_tv_show_table_builder = BrowseTvShowTableBuilder()
    if len(results) > 0:
        table = browse_tv_show_table_builder.build(tv_shows=results)
        click.echo(table)


@click.command()
@click.argument("category", default="new_tonight", type=click.Choice(["new_tonight", "most_popular", "certified_fresh"]))
def movie(category):
    click.echo("movies")


browse.add_command(tv)
browse.add_command(movie)