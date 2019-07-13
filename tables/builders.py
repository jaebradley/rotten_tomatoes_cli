from terminaltables import SingleTable

from tables.utilities import formatted_header


class RottenTomatoesTableBuilder:
    def __init__(self, row_builder):
        self.row_builder = row_builder

    def build(self, objects):
        table = SingleTable(self.all_table_rows(objects))
        table.justify_columns = self.column_format()
        table.inner_row_border = True
        return table.table

    def all_table_rows(self, objects):
        return [self.formatted_headers()] + self.rows(objects)

    def formatted_headers(self):
        return [formatted_header(text=value) for value in self.header_values()]

    def rows(self, objects):
        return [
            self.row_builder.build(obj)
            for obj in RottenTomatoesTableBuilder.sort_by_score_descending(objects)
        ]

    @staticmethod
    def sort_by_score_descending(objects):
        return sorted(
                objects,
                key=lambda obj: obj.rotten_tomatoes_score if obj.rotten_tomatoes_score is not None else -1,
                reverse=True
        )

    @staticmethod
    def column_format():
        return {}

    @staticmethod
    def header_values():
        return []


class MovieSearchTableBuilder(RottenTomatoesTableBuilder):

    @staticmethod
    def column_format():
        return {2: "center"}

    @staticmethod
    def header_values():
        return ["Film", "Score", "Year", "Cast"]


class TvShowSearchTableBuilder(RottenTomatoesTableBuilder):

    @staticmethod
    def header_values():
        return ["TV Show", "Score", "Years"]


class BrowseTvShowTableBuilder(RottenTomatoesTableBuilder):

    @staticmethod
    def header_values():
        return ["TV Show", "Score"]


class BrowseMovieTableBuilder(RottenTomatoesTableBuilder):

    @staticmethod
    def header_values():
        return ["", "Details"]
