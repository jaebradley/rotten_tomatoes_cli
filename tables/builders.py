from terminaltables import SingleTable
import emoji
from termcolor import colored, cprint

from tables.rows.builders import MovieSearchRowBuilder


class MovieSearchTableBuilder:
    HEADERS = ["Film","Score", "Year", "Cast"]
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
        return [self.row_builder.build(data=movie) for movie in sorted_movies]