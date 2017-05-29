from terminaltables import SingleTable
from termcolor import colored

from tables.rows.builders import MovieSearchRowBuilder, TvShowSearchRowBuilder, BrowseTvShowRowBuilder, \
    BrowseMovieRowBuilder


class MovieSearchTableBuilder:
    HEADERS = ["Film", "Score", "Year", "Cast"]
    COLUMN_JUSTIFICATION = {
        0: "left",
        1: "left",
        2: "center",
        3: "left"
    }

    def __init__(self):
        self.row_builder = MovieSearchRowBuilder()

    def build(self, movies):
        table = SingleTable([MovieSearchTableBuilder.HEADERS] + self.rows(movies=movies))
        table.justify_columns = MovieSearchTableBuilder.COLUMN_JUSTIFICATION
        return table.table

    def rows(self, movies):
        sorted_movies = sorted(movies, key=lambda movie: movie.rotten_tomatoes_score, reverse=True)
        return [self.row_builder.build(movie=movie) for movie in sorted_movies]


class TvShowSearchTableBuilder:
    HEADERS = ["TV Show", "Score", "Years"]
    COLUMN_JUSTIFICATION = {
        0: "left",
        1: "left",
        2: "left",
    }

    def __init__(self):
        self.row_builder = TvShowSearchRowBuilder()

    def build(self, tv_shows):
        table = SingleTable([TvShowSearchTableBuilder.HEADERS] + self.rows(tv_shows=tv_shows))
        table.justify_columns = TvShowSearchTableBuilder.COLUMN_JUSTIFICATION
        return table.table

    def rows(self, tv_shows):
        sorted_tv_shows = sorted(tv_shows, key=lambda tv_show: tv_show.rotten_tomatoes_score, reverse=True)
        return [self.row_builder.build(tv_show=tv_show) for tv_show in sorted_tv_shows]


class BrowseTvShowTableBuilder:
    HEADERS = ["TV Show", "Score"]
    COLUMN_JUSTIFICATION = {
        0: "left",
        1: "left",
    }

    def __init__(self):
        self.row_builder = BrowseTvShowRowBuilder()

    def build(self, tv_shows):
        table = SingleTable([BrowseTvShowTableBuilder.HEADERS] + self.rows(tv_shows=tv_shows))
        table.justify_columns = BrowseTvShowTableBuilder.COLUMN_JUSTIFICATION
        return table.table

    def rows(self, tv_shows):
        sorted_tv_shows = sorted(tv_shows, key=lambda tv_show: tv_show.rotten_tomatoes_score, reverse=True)
        return [self.row_builder.build(tv_show=tv_show) for tv_show in sorted_tv_shows]


class BrowseMovieTableBuilder:
    HEADERS = ["", colored("Details", attrs=["bold", "underline"])]
    COLUMN_JUSTIFICATION = {
        0: "left",
        1: "left",
    }

    def __init__(self):
        self.row_builder = BrowseMovieRowBuilder()

    def build(self, movies):
        table = SingleTable([BrowseMovieTableBuilder.HEADERS] + self.rows(movies=movies))
        table.justify_columns = BrowseMovieTableBuilder.COLUMN_JUSTIFICATION
        table.inner_row_border = True
        return table.table

    def rows(self, movies):
        sorted_movies = sorted(movies, key=lambda movie: movie.rotten_tomatoes_score, reverse=True)
        return [self.row_builder.build(movie=movie) for movie in sorted_movies]
