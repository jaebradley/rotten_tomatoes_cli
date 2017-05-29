from enum import Enum

from rotten_tomatoes_client import TvBrowsingCategory, MovieBrowsingCategory


class MovieSearchResult:
    def __init__(self, name, year, rotten_tomatoes_score, cast):
        self.name = name
        self.year = year
        self.rotten_tomatoes_score = rotten_tomatoes_score
        self.cast = cast


class TvShowSearchResult:
    def __init__(self, name, start_year, end_year, rotten_tomatoes_score):
        self.name = name
        self.start_year = start_year
        self.end_year = end_year
        self.rotten_tomatoes_score = rotten_tomatoes_score


class SearchResult:
    def __init__(self, movies, tv_shows):
        self.movies = movies
        self.tv_shows = tv_shows


class BrowseMovieResult:
    def __init__(self, title, rotten_tomatoes_score, synopsis, runtime, theater_release_date, dvd_release_date, mpaa_rating):
        self.title = title
        self.rotten_tomatoes_score = rotten_tomatoes_score
        self.synopsis = synopsis
        self.runtime = runtime
        self.theater_release_date = theater_release_date
        self.dvd_release_date = dvd_release_date
        self.mpaa_rating = mpaa_rating


class BrowseTvShowResult:
    def __init__(self, title, rotten_tomatoes_score):
        self.title = title
        self.rotten_tomatoes_score = rotten_tomatoes_score


class BrowseTvShowCategory(Enum):

    new = {
        "value": "new",
        "client_value": TvBrowsingCategory.new_tv_tonight
    },
    popular = {
        "value": "popular",
        "client_value": TvBrowsingCategory.most_popular
    },
    fresh = {
        "value": "fresh",
        "client_value": TvBrowsingCategory.certified_fresh
    }

    @staticmethod
    def values():
        return [category["value"] for category in BrowseTvShowCategory]

    @staticmethod
    def category(value):
        for category in BrowseTvShowCategory:
            if category["value"] == value:
                return category

        raise LookupError("Unknown category for value: {value}".format(value=value))


class BrowseMovieInTheaterCategory(Enum):
    opening = {
        "value": "opening",
        "client_value": MovieBrowsingCategory.opening_in_theaters
    },
    playing = {
        "value": "playing",
        "client_value": MovieBrowsingCategory.in_theaters
    },
    upcoming = {
        "value": "upcoming",
        "client_value": MovieBrowsingCategory.upcoming_in_theaters
    },
    fresh = {
        "value": "fresh",
        "client_value": MovieBrowsingCategory.certified_fresh_in_theaters
    }

    @staticmethod
    def values():
        return [category["value"] for category in BrowseMovieInTheaterCategory]

    @staticmethod
    def category(value):
        for category in BrowseMovieInTheaterCategory:
            if category["value"] == value:
                return category

        raise LookupError("Unknown category for value: {value}".format(value=value))


class BrowseStreamingMovieCategory(Enum):
    all = {
        "value": "all",
        "client_value": MovieBrowsingCategory.all_dvd_and_streaming
    },
    top = {
        "value": "top",
        "client_value": MovieBrowsingCategory.top_dvd_and_streaming
    },
    new = {
        "value": "new",
        "client_value": MovieBrowsingCategory.new_dvd_and_streaming
    },
    upcoming = {
        "value": "upcoming",
        "client_value": MovieBrowsingCategory.upcoming_dvd_and_streaming
    },
    fresh = {
        "value": "fresh",
        "client_value": MovieBrowsingCategory.certified_fresh_dvd_and_streaming
    }

    @staticmethod
    def values():
        return [category["value"] for category in BrowseStreamingMovieCategory]

    @staticmethod
    def category(value):
        for category in BrowseStreamingMovieCategory:
            if category["value"] == value:
                return category

        raise LookupError("Unknown category for value: {value}".format(value=value))