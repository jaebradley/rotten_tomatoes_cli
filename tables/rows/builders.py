from textwrap import wrap

from termcolor import colored

from tables.utilities import RottenTomatoesScoreFormatter, MpaaRatingFormatter, convert_to_ascii, clean_html, formatted_header


class MovieSearchRowBuilder:

    def __init__(self):
        self.rating_formatter = RottenTomatoesScoreFormatter()

    def build(self, movie):
        return [
            self.name(name=movie.name),
            self.rating_formatter.format(rating=movie.rotten_tomatoes_score),
            movie.year,
            self.cast(cast=movie.cast)
        ]

    def name(self, name):
        wrapped_name = wrap(text=convert_to_ascii(text=name), width=30)
        return "\n".join([colored(value, attrs=["bold"]) for value in wrapped_name])

    def cast(self, cast):
        return "\n".join([convert_to_ascii(text=actor) for actor in cast])


class TvShowSearchRowBuilder:
    def __init__(self):
        self.rating_formatter = RottenTomatoesScoreFormatter()

    def build(self, tv_show):
        return [
            self.name(name=tv_show.name),
            self.rating_formatter.format(rating=tv_show.rotten_tomatoes_score),
            self.format_years(start_year=tv_show.start_year, end_year=tv_show.end_year)
        ]

    def format_years(self, start_year, end_year):
        end_year_value = "" if end_year is None else end_year
        return "{start_year}-{end_year}".format(start_year=start_year, end_year=end_year_value)

    def name(self, name):
        wrapped_name = wrap(text=convert_to_ascii(text=name), width=30)
        return "\n".join([colored(value, attrs=["bold"]) for value in wrapped_name])


class BrowseTvShowRowBuilder:
    def __init__(self):
        self.rating_formatter = RottenTomatoesScoreFormatter()

    def build(self, tv_show):
        return [tv_show.title, self.rating_formatter.format(rating=tv_show.rotten_tomatoes_score)]


class BrowseMovieRowBuilder:

    def __init__(self):
        self.rotten_tomatoes_score_formatter = RottenTomatoesScoreFormatter()
        self.mpaa_rating_formatter = MpaaRatingFormatter()

    def build(self, movie):
        return [
            self.summary(movie=movie),
            self.details(movie=movie)
        ]

    def summary(self, movie):
        return "{title}\n\n" \
               "{synopsis}"\
            .format(title=self.title(title=movie.title),
                    synopsis=self.synopsis(synopsis=movie.synopsis))

    def details(self, movie):
        return "{score_header}\n" \
               "{score}\n\n" \
               "{rating_header}\n" \
               "{rating}\n\n" \
               "{runtime_header}\n" \
               "{runtime}\n\n" \
               "{release_header}\n" \
               "{release}\n\n" \
               "{actors_header}\n" \
               "{actors}"\
            .format(score_header=formatted_header(text="Score"),
                    rating_header=formatted_header(text="Rating"),
                    runtime_header=formatted_header(text="Runtime"),
                    release_header=formatted_header(text="Release"),
                    actors_header=formatted_header(text="Actors"),
                    score=self.rotten_tomatoes_score_formatter.format(rating=movie.rotten_tomatoes_score),
                    rating=self.mpaa_rating_formatter.format(rating=movie.mpaa_rating),
                    runtime=self.runtime(runtime=movie.runtime),
                    release=self.release_dates(movie=movie),
                    actors=self.actors(actors=movie.actors))

    def release_dates(self, movie):
        release_dates = []

        if movie.theater_release_date is not None:
            release_dates.append("{theater_release_date} (Theaters)"
                                 .format(theater_release_date=movie.theater_release_date))

        if movie.dvd_release_date is not None:
            release_dates.append("{dvd_release_date} (DVD)".format(dvd_release_date=movie.dvd_release_date))

        return "\n".join(release_dates)

    def actors(self, actors):
        return "\n".join([convert_to_ascii(text=actor) for actor in actors])

    def runtime(self, runtime):
        return "N/A" if runtime is None else runtime

    def synopsis(self, synopsis):
        return "\n".join(wrap(text=convert_to_ascii(text=clean_html(raw_html=synopsis)), width=50))

    def title(self, title):
        wrapped_title = wrap(text=convert_to_ascii(text=title), width=50)
        return "\n".join([colored(value, attrs=["bold", "underline"]) for value in wrapped_title])
