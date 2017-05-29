import click

from data import BrowseStreamingMovieCategory, BrowseMovieInTheaterCategory, MovieService, MovieGenre, BrowseSortBy
from data.services import RottenTomatoesMoviesBrowser
from rotten_tomatoes_client import MovieBrowsingQuery
from tables.builders import BrowseMovieTableBuilder


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
    context.obj["SORT_BY"] = sort_by


@click.command()
@click.argument("category", default=BrowseMovieInTheaterCategory.opening.name, type=click.Choice(BrowseMovieInTheaterCategory.names()))
@click.pass_context
def in_theaters(context, category):
    services = [service[0]["client_service"] for service in context.obj["SERVICE"]]
    genres = [genre[0]["client_genre"] for genre in context.obj["GENRE"]]
    query = MovieBrowsingQuery(minimum_rating=context.obj["MINIMUM_RATING"],
                               maximum_rating=context.obj["MAXIMUM_RATING"],
                               certified_fresh=context.obj["CERTIFIED_FRESH"], services=services, genres=genres,
                               sort_by=context.obj["SORT_BY"][0]["client_value"],
                               category=category[0]["client_category"])
    browser = RottenTomatoesMoviesBrowser()
    results = browser.browse(query=query)
    table_builder = BrowseMovieTableBuilder()
    click.echo(table_builder.build(movies=results))


@click.command()
@click.argument("category", default=BrowseStreamingMovieCategory.new.name, type=click.Choice(BrowseStreamingMovieCategory.names()))
@click.pass_context
def streaming(context, category):
    services = [MovieService.service(value=service).value[0]["client_service"] for service in context.obj["SERVICE"]]
    genres = [MovieGenre.genre(value=genre).value[0]["client_genre"] for genre in context.obj["GENRE"]]
    query = MovieBrowsingQuery(minimum_rating=context.obj["MINIMUM_RATING"],
                               maximum_rating=context.obj["MAXIMUM_RATING"],
                               certified_fresh=context.obj["CERTIFIED_FRESH"], services=services, genres=genres,
                               sort_by=BrowseSortBy.sort_by(value=context.obj["SORT_BY"]).value[0]["client_value"],
                               category=BrowseStreamingMovieCategory.category(value=category).value[0]["client_category"])
    browser = RottenTomatoesMoviesBrowser()
    results = browser.browse(query=query)
    table_builder = BrowseMovieTableBuilder()
    click.echo(table_builder.build(movies=results))



movies.add_command(in_theaters)
movies.add_command(streaming)