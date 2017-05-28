from terminaltables import SingleTable
import emoji
from termcolor import colored, cprint

from tables.rows.builders import MovieSearchRowBuilder


class MovieSearchTableBuilder:
    HEADERS = [emoji.emojize(":movie_camera:", use_aliases=True), emoji.emojize(":tomato:", use_aliases=True), "Year",
               emoji.emojize(":busts_in_silhouette:", use_aliases=True)]

    def __init__(self):
        self.row_builder = MovieSearchRowBuilder()

    def build(self, movies):
        self.rows(movies=movies)
        table = SingleTable([[colored('Film', 'red'),"Score", "Year", "Cast"]] + self.rows(movies=movies))
        table.justify_columns = {
            0: "left",
            1: "center",
            2: "center",
            3: "left"
        }
        return table.table

    def rows(self, movies):
        sorted_movies = sorted(movies, key=lambda movie: movie.rotten_tomatoes_score, reverse=True)
        return [self.row_builder.build(data=movie) for movie in sorted_movies]