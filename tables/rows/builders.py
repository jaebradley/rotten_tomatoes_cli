from tables.utilities import RatingFormatter


class MovieSearchRowBuilder:

    def __init__(self):
        self.rating_formatter = RatingFormatter()

    def build(self, data):
        return [data.name, self.rating_formatter.format(rating=data.rotten_tomatoes_score), data.year, ", ".join(data.cast)]
