from tables.utilities import RatingFormatter


class MovieSearchRowBuilder:

    def __init__(self):
        self.rating_formatter = RatingFormatter()

    def build(self, data):
        return [data.name, self.rating_formatter.format(rating=data.rotten_tomatoes_score), data.year, ", ".join(data.cast)]


class TvShowSearchRowBuilder:
    def __init__(self):
        self.rating_formatter = RatingFormatter()

    def build(self, tv_show):
        return [tv_show.name, self.rating_formatter.format(rating=tv_show.rotten_tomatoes_score),
                self.format_years(start_year=tv_show.start_year, end_year=tv_show.end_year)]

    def format_years(self, start_year, end_year):
        end_year_value = "" if end_year is None else end_year
        return "{start_year}-{end_year}".format(start_year=start_year, end_year=end_year_value)