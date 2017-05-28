from tables.utilities import RatingFormatter


class MovieSearchRowBuilder:

    def __init__(self):
        self.rating_formatter = RatingFormatter()

    def build(self, data):
        return [data.title, self.rating_formatter.format(rating=data.rating), data.year, data.cast]

