from tabulate import tabulate
import emoji

from tables.rows.builders import MovieSearchRowBuilder


class MovieSearchTableBuilder:
    HEADERS = [emoji.emojize(":movie_camera"), emoji.emojize(":tomato:"), "Year", emoji.emojize(":busts_in_silhouette:")]

    def __init__(self):
        self.row_builder = MovieSearchRowBuilder()

    def build(self, data):
        return tabulate(tabular_data=self.rows(data=data), headers=MovieSearchTableBuilder.HEADERS,
                        tablefmt="fancy_grid")

    def rows(self, data):
        return [self.row_builder.build(data=movie) for movie in data.movies]