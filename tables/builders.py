from terminaltables import SingleTable

from tables.utilities import formatted_header


class RottenTomatoesTableBuilder:
    def __init__(self, row_builder):
        self.row_builder = row_builder

    def build(self, objects):
        table = SingleTable(self.all_table_rows(objects))
        print self.all_table_rows(objects)
        table.justify_columns = self.column_format()
        table.inner_row_border = True
        return table.table

    def all_table_rows(self, objects):
        return [self.headers()] + self.rows(objects)

    def rows(self, objects):
        return [
            self.row_builder.build(obj)
            for obj in RottenTomatoesTableBuilder.sort_by_score_descending(objects)
        ]

    @staticmethod
    def sort_by_score_descending(objects):
        return sorted(objects, key=lambda obj: obj.rotten_tomatoes_score, reverse=True)

    @staticmethod
    def column_format():
        return {}

    @staticmethod
    def headers():
        return []


class MovieSearchTableBuilder(RottenTomatoesTableBuilder):

    @staticmethod
    def column_format():
        return {2: "center"}

    @staticmethod
    def headers():
        return [
            formatted_header(text="Film"),
            formatted_header(text="Score"),
            formatted_header(text="Year"),
            formatted_header(text="Cast")
        ]


class TvShowSearchTableBuilder(RottenTomatoesTableBuilder):

    @staticmethod
    def headers():
        return [
            formatted_header("TV Show"),
            formatted_header("Score"),
            formatted_header("Years")
        ]


class BrowseTvShowTableBuilder(RottenTomatoesTableBuilder):

    @staticmethod
    def headers():
        return [
            formatted_header(text="TV Show"),
            formatted_header(text="Score")
        ]


class BrowseMovieTableBuilder(RottenTomatoesTableBuilder):

    @staticmethod
    def headers():
        return ["", formatted_header(text="Details")]
