from terminaltables import SingleTable

from tables.rows.builders import MovieSearchRowBuilder, TvShowSearchRowBuilder, BrowseTvShowRowBuilder, \
    BrowseMovieRowBuilder
from tables.utilities import formatted_header


class RottenTomatoesScoreSorter:
    def __init__(self):
        pass

    def sort_descending(self, objects):
        return sorted(objects, key=lambda obj: obj.rotten_tomatoes_score, reverse=True)


class MovieSearchTableBuilder(RottenTomatoesScoreSorter):
    HEADERS = [
        formatted_header(text="Film"),
        formatted_header(text="Score"),
        formatted_header(text="Year"),
        formatted_header(text="Cast")
    ]
    COLUMN_JUSTIFICATION = {2: "center"}

    def __init__(self):
        RottenTomatoesScoreSorter.__init__(self)
        self.row_builder = MovieSearchRowBuilder()

    def build(self, movies):
        table = SingleTable([MovieSearchTableBuilder.HEADERS] + self.rows(movies))
        table.justify_columns = MovieSearchTableBuilder.COLUMN_JUSTIFICATION
        table.inner_row_border = True
        return table.table

    def rows(self, movies):
        return [
            self.row_builder.build(movie)
            for movie in self.sort_descending(movies)
        ]


class TvShowSearchTableBuilder(RottenTomatoesScoreSorter):
    HEADERS = [formatted_header(text="TV Show"), formatted_header(text="Score"), formatted_header(text="Years")]

    def __init__(self):
        RottenTomatoesScoreSorter.__init__(self)
        self.row_builder = TvShowSearchRowBuilder()

    def build(self, tv_shows):
        table = SingleTable([TvShowSearchTableBuilder.HEADERS] + self.rows(tv_shows=tv_shows))
        table.inner_row_border = True
        return table.table

    def rows(self, tv_shows):
        sorted_tv_shows = sorted(tv_shows, key=lambda tv_show: tv_show.rotten_tomatoes_score, reverse=True)
        return [self.row_builder.build(tv_show=tv_show) for tv_show in sorted_tv_shows]


class BrowseTvShowTableBuilder(RottenTomatoesScoreSorter):
    HEADERS = [formatted_header(text="TV Show"), formatted_header(text="Score")]

    def __init__(self):
        RottenTomatoesScoreSorter.__init__(self)
        self.row_builder = BrowseTvShowRowBuilder()

    def build(self, tv_shows):
        table = SingleTable([BrowseTvShowTableBuilder.HEADERS] + self.rows(tv_shows=tv_shows))
        table.inner_row_border = True
        return table.table

    def rows(self, tv_shows):
        sorted_tv_shows = sorted(tv_shows, key=lambda tv_show: tv_show.rotten_tomatoes_score, reverse=True)
        return [self.row_builder.build(tv_show=tv_show) for tv_show in sorted_tv_shows]


class BrowseMovieTableBuilder(RottenTomatoesScoreSorter):
    HEADERS = ["", formatted_header(text="Details")]

    def __init__(self):
        RottenTomatoesScoreSorter.__init__(self)
        self.row_builder = BrowseMovieRowBuilder()

    def build(self, movies):
        table = SingleTable([BrowseMovieTableBuilder.HEADERS] + self.rows(movies=movies))
        table.inner_row_border = True
        return table.table

    def rows(self, movies):
        sorted_movies = sorted(movies, key=lambda movie: movie.rotten_tomatoes_score, reverse=True)
        return [self.row_builder.build(movie=movie) for movie in sorted_movies]
