from termcolor import colored

from tables.utilities import RatingFormatter


class MovieSearchRowBuilder:

    def __init__(self):
        self.rating_formatter = RatingFormatter()

    def build(self, movie):
        return [movie.name, self.rating_formatter.format(rating=movie.rotten_tomatoes_score), movie.year, ", ".join(movie.cast)]


class TvShowSearchRowBuilder:
    def __init__(self):
        self.rating_formatter = RatingFormatter()

    def build(self, tv_show):
        return [tv_show.name, self.rating_formatter.format(rating=tv_show.rotten_tomatoes_score),
                self.format_years(start_year=tv_show.start_year, end_year=tv_show.end_year)]

    def format_years(self, start_year, end_year):
        end_year_value = "" if end_year is None else end_year
        return "{start_year}-{end_year}".format(start_year=start_year, end_year=end_year_value)


class BrowseTvShowRowBuilder:
    def __init__(self):
        self.rating_formatter = RatingFormatter()

    def build(self, tv_show):
        return [tv_show.title, self.rating_formatter.format(rating=tv_show.rotten_tomatoes_score)]


class BrowseMovieRowBuilder:
    def __init__(self):
        self.rating_formatter = RatingFormatter()

    def build(self, movie):
        return [self.title(movie=movie), self.rating_formatter.format(rating=movie.rotten_tomatoes_score),
                movie.runtime, self.release_dates(movie=movie), self.actors(actors=movie.actors)]

    def title(self, movie):
        return "{title} ({rating})".format(title=colored(movie.title, attrs=["bold"]), rating=movie.mpaa_rating)

    def release_dates(self, movie):
        release_dates = []
        if movie.theater_release_date is not None:
            release_dates.append("{theater_release_date} (Theaters)".format(theater_release_date=movie.theater_release_date))
        if movie.dvd_release_date is not None:
            release_dates.append("{dvd_release_date} (DVD)".format(dvd_release_date=movie.dvd_release_date))

        return "\n".join(release_dates)

    def actors(self, actors):
        return ",\n".join(actors)