import click

from data.services import RottenTomatoesSearcher
from tables.builders import MovieSearchTableBuilder, TvShowSearchTableBuilder
from tables.rows.builders import MovieSearchRowBuilder, TvShowSearchRowBuilder

searcher = RottenTomatoesSearcher()
movie_search_table_builder = MovieSearchTableBuilder(MovieSearchRowBuilder())
tv_show_search_table_builder = TvShowSearchTableBuilder(TvShowSearchRowBuilder())


@click.command()
@click.argument("term", type=click.STRING)
def search(term):
    results = searcher.search(term=term)

    if len(results.movies) > 0:
        movie_search_table = movie_search_table_builder.build(results.movies)
        click.echo(movie_search_table)

    if len(results.tv_shows) > 0:
        tv_show_search_table = tv_show_search_table_builder.build(results.tv_shows)
        click.echo(tv_show_search_table)
