import click

from data import BrowseStreamingMovieCategory, BrowseMovieInTheaterCategory, MovieService


@click.group()
@click.option("--minimum_rating", "-min", default=70)
@click.option("--maximum_rating", "-max", default=100)
@click.option("--certified_fresh", "-f", default=False)
@click.option("--service", "-s", multiple=True, type=click.Choice(MovieService.values()))
@click.option("--genre", "-g", multiple=True)
@click.option("--sort_by", "-sb")
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