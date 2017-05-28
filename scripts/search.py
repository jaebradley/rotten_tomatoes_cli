import click

from data.services import RottenTomatoesSearcher
from tables.builders import MovieSearchTableBuilder


@click.command
def search(term):
    searcher = RottenTomatoesSearcher()
    movie_search_table_builder = MovieSearchTableBuilder()
    results = searcher.search(term=term)
    movie_search_table = movie_search_table_builder.build(data=results.movies)
    click.echo(movie_search_table)