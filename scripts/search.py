import click

from data.services import RottenTomatoesSearcher
from tables.builders import MovieSearchTableBuilder


@click.command()
@click.argument("term", type=click.STRING)
def search(term):
    searcher = RottenTomatoesSearcher()
    movie_search_table_builder = MovieSearchTableBuilder()
    results = searcher.search(term=term)
    movie_search_table = movie_search_table_builder.build(movies=results.movies)
    click.echo(movie_search_table)
