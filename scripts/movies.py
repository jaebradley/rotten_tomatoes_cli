import click
from rotten_tomatoes_client import MovieBrowsingQuery

from data import BrowseStreamingMovieCategory, BrowseMovieInTheaterCategory, MovieService, MovieGenre, BrowseSortBy
from data.services import RottenTomatoesMoviesBrowser
from tables.builders import BrowseMovieTableBuilder
from tables.rows.builders import BrowseMovieRowBuilder

browser = RottenTomatoesMoviesBrowser()
table_builder = BrowseMovieTableBuilder(BrowseMovieRowBuilder())


@click.group()
def movies():
    pass


@click.command()
@click.argument("category", default=BrowseMovieInTheaterCategory.opening.name,
                type=click.Choice(BrowseMovieInTheaterCategory.names()))
@click.option("--minimum_rating", "-l", default=70)
@click.option("--maximum_rating", "-h", default=100)
@click.option("--certified_fresh", "-f", is_flag=True)
@click.option("--service", "-s", default=None, multiple=True, type=click.Choice(MovieService.names()))
@click.option("--genre", "-g", default=None, multiple=True, type=click.Choice(MovieGenre.names()))
@click.option("--sort_by", default=BrowseSortBy.popularity.name, type=click.Choice(BrowseSortBy.names()))
def theaters(category, minimum_rating, maximum_rating, certified_fresh, service, genre, sort_by):
    theaters_category = BrowseMovieInTheaterCategory.category(value=category).value["client_category"]
    build(category=theaters_category, minimum_rating=minimum_rating, maximum_rating=maximum_rating,
          certified_fresh=certified_fresh, services=service, genres=genre, sort_by=sort_by)


@click.command()
@click.argument("category", default=BrowseStreamingMovieCategory.new.name,
                type=click.Choice(BrowseStreamingMovieCategory.names()))
@click.option("--minimum_rating", "-l", default=70)
@click.option("--maximum_rating", "-h", default=100)
@click.option("--certified_fresh", "-f", is_flag=True)
@click.option("--service", "-s", default=None, multiple=True, type=click.Choice(MovieService.names()))
@click.option("--genre", "-g", default=None, multiple=True, type=click.Choice(MovieGenre.names()))
@click.option("--sort_by", default=BrowseSortBy.popularity.name, type=click.Choice(BrowseSortBy.names()))
def streaming(category, minimum_rating, maximum_rating, certified_fresh, service, genre, sort_by):
    streaming_category = BrowseStreamingMovieCategory.category(value=category).value["client_category"]
    build(category=streaming_category, minimum_rating=minimum_rating, maximum_rating=maximum_rating,
          certified_fresh=certified_fresh, services=service, genres=genre, sort_by=sort_by)


def build(category, minimum_rating, maximum_rating, certified_fresh, services, genres, sort_by):
    results = browser.browse(query(category=category, minimum_rating=minimum_rating,
                                   maximum_rating=maximum_rating, certified_fresh=certified_fresh,
                                   services=services, genres=genres, sort_by=sort_by))
    if len(results) > 0:
        click.echo(table_builder.build(results))
    else:
        click.echo("No results")


def query(category, minimum_rating, maximum_rating, certified_fresh, services, genres, sort_by):
    services = [MovieService.service(value=service).value["client_service"] for service in services]
    genres = [MovieGenre.genre(value=genre).value["client_genre"] for genre in genres]
    return MovieBrowsingQuery(minimum_rating=minimum_rating,
                              maximum_rating=maximum_rating,
                              certified_fresh=certified_fresh, services=services, genres=genres,
                              sort_by=BrowseSortBy.sort_by(value=sort_by).value["client_value"],
                              category=category)


movies.add_command(theaters)
movies.add_command(streaming)
