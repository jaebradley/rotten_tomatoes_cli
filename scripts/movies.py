import click

from data import BrowseStreamingMovieCategory, BrowseMovieInTheaterCategory, MovieService, MovieGenre, BrowseSortBy


@click.group()
@click.option("--minimum_rating", "-min", default=70)
@click.option("--maximum_rating", "-max", default=100)
@click.option("--certified_fresh", "-f", default=False)
@click.option("--service", "-s", default=None, multiple=True, type=click.Choice(MovieService.names()))
@click.option("--genre", "-g", default=None, multiple=True, type=click.Choice(MovieGenre.names()))
@click.option("--sort_by", "-sb", default=BrowseSortBy.popularity.name, type=click.Choice(BrowseSortBy.names()))
@click.pass_context
def movies(context, minimum_rating, maximum_rating, certified_fresh, service, genre, sort_by):
    context.obj = {}
    context.obj["MINIMUM_RATING"] = minimum_rating
    context.obj["MAXIMUM_RATING"] = maximum_rating
    context.obj["CERTIFIED_FRESH"] = certified_fresh
    context.obj["SERVICE"] = service
    context.obj["GENRE"] = genre
    context.obj["SORT)BY"] = sort_by


@click.command()
@click.argument("category", default=BrowseMovieInTheaterCategory.opening.name, type=click.Choice(BrowseMovieInTheaterCategory.names()))
@click.pass_context
def in_theaters(context, category):
    click.echo(context)
    click.echo("movies in theaters")


@click.command()
@click.argument("category", default=BrowseStreamingMovieCategory.new.name, type=click.Choice(BrowseStreamingMovieCategory.names()))
@click.pass_context
def streaming(context, category):
    click.echo("streaming movies")



movies.add_command(in_theaters)
movies.add_command(streaming)