import click

from data import BrowseStreamingMovieCategory, BrowseMovieInTheaterCategory


@click.group()
def movies():
    pass


@click.command()
@click.argument("category", default=BrowseMovieInTheaterCategory.opening["value"], type=click.Choice(BrowseMovieInTheaterCategory.values()))
def in_theaters(category):
    click.echo("movies in theaters")

@click.command()
@click.argument("category", default=BrowseStreamingMovieCategory.new["value"], type=click.Choice(BrowseStreamingMovieCategory.values()))
def streaming(category):
    click.echo("streaming movies")



movies.add_command(in_theaters)
movies.add_command(streaming)