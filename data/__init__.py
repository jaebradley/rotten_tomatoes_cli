from enum import Enum

from rotten_tomatoes_client import TvBrowsingCategory, MovieBrowsingCategory, Service, Genre, SortBy


class MovieSearchResult:
    def __init__(self, name, year, rotten_tomatoes_score, cast):
        self.name = name
        self.year = year
        self.rotten_tomatoes_score = rotten_tomatoes_score
        self.cast = cast

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class TvShowSearchResult:
    def __init__(self, name, start_year, end_year, rotten_tomatoes_score):
        self.name = name
        self.start_year = start_year
        self.end_year = end_year
        self.rotten_tomatoes_score = rotten_tomatoes_score

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class SearchResult:
    def __init__(self, movies, tv_shows):
        self.movies = movies
        self.tv_shows = tv_shows

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class BrowseMovieResult:
    def __init__(self, title, rotten_tomatoes_score, synopsis, runtime, theater_release_date, dvd_release_date,
                 mpaa_rating, actors):
        self.title = title
        self.rotten_tomatoes_score = rotten_tomatoes_score
        self.synopsis = synopsis
        self.runtime = runtime
        self.theater_release_date = theater_release_date
        self.dvd_release_date = dvd_release_date
        self.mpaa_rating = mpaa_rating
        self.actors = actors

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class BrowseTvShowResult:
    def __init__(self, title, rotten_tomatoes_score):
        self.title = title
        self.rotten_tomatoes_score = rotten_tomatoes_score

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class BrowseTvShowCategory(Enum):
    new = {
        "client_category": TvBrowsingCategory.new_tv_tonight
    }
    popular = {
        "client_category": TvBrowsingCategory.most_popular
    }
    fresh = {
        "client_category": TvBrowsingCategory.certified_fresh
    }

    @staticmethod
    def names():
        return [category.name for category in BrowseTvShowCategory]

    @staticmethod
    def category(value):
        for category in BrowseTvShowCategory:
            if category.name == value.lower():
                return category

        raise LookupError("Unknown tv show category for value: {value}".format(value=value))


class BrowseMovieInTheaterCategory(Enum):
    opening = {
        "client_category": MovieBrowsingCategory.opening_in_theaters
    }
    playing = {
        "client_category": MovieBrowsingCategory.in_theaters
    }
    upcoming = {
        "client_category": MovieBrowsingCategory.upcoming_in_theaters
    }
    fresh = {
        "client_category": MovieBrowsingCategory.certified_fresh_in_theaters
    }

    @staticmethod
    def names():
        return [category.name for category in BrowseMovieInTheaterCategory]

    @staticmethod
    def category(value):
        for category in BrowseMovieInTheaterCategory:
            if category.name == value.lower():
                return category

        raise LookupError("Unknown movie in theater category for value: {value}".format(value=value))


class BrowseStreamingMovieCategory(Enum):
    all = {
        "client_category": MovieBrowsingCategory.all_dvd_and_streaming
    }
    top = {
        "client_category": MovieBrowsingCategory.top_dvd_and_streaming
    }
    new = {
        "client_category": MovieBrowsingCategory.new_dvd_and_streaming
    }
    upcoming = {
        "client_category": MovieBrowsingCategory.upcoming_dvd_and_streaming
    }
    fresh = {
        "client_category": MovieBrowsingCategory.certified_fresh_dvd_and_streaming
    }

    @staticmethod
    def names():
        return [category.name for category in BrowseStreamingMovieCategory]

    @staticmethod
    def category(value):
        for category in BrowseStreamingMovieCategory:
            if category.name == value.lower():
                return category

        raise LookupError("Unknown streaming movie category for value: {value}".format(value=value))


class MovieService(Enum):
    amazon = {
        "client_service": Service.amazon
    }
    prime = {
        "client_service": Service.amazon_prime
    }
    hbo = {
        "client_service": Service.hbo_go
    }
    itunes = {
        "client_service": Service.itunes
    }
    netflix = {
        "client_service": Service.netflix
    }
    vudu = {
        "client_service": Service.vudu
    }
    fandango = {
        "client_service": Service.fandango_now
    }

    @staticmethod
    def names():
        return [service.name for service in MovieService]

    @staticmethod
    def service(value):
        for service in MovieService:
            if service.name == value.lower():
                return service

        raise LookupError("Unknown movie service for value: {value}".format(value=value))


class MovieGenre(Enum):
    action = {
        "client_genre": Genre.action
    }
    animation = {
        "client_genre": Genre.animation
    }
    art_and_foreign = {
        "client_genre": Genre.art_and_foreign
    }
    classics = {
        "client_genre": Genre.classics
    }
    comedy = {
        "client_genre": Genre.comedy
    }
    documentary = {
        "client_genre": Genre.documentary
    }
    drama = {
        "client_genre": Genre.drama
    }
    horror = {
        "client_genre": Genre.horror
    }
    family = {
        "client_genre": Genre.kids_and_family
    }
    mystery = {
        "client_genre": Genre.mystery
    }
    romance = {
        "client_genre": Genre.romance
    }
    scifi = {
        "client_genre": Genre.sci_fi_and_fantasy
    }

    @staticmethod
    def names():
        return [genre.name for genre in MovieGenre]

    @staticmethod
    def genre(value):
        for genre in MovieGenre:
            if genre.name == value.lower():
                return genre

        raise LookupError("Unknown movie genre for value: {value}".format(value=value))


class BrowseSortBy(Enum):
    popularity = {
        "client_value": SortBy.popularity
    }
    release = {
        "client_value": SortBy.release
    }

    @staticmethod
    def names():
        return [sort_by.name for sort_by in BrowseSortBy]

    @staticmethod
    def sort_by(value):
        for sort_by in BrowseSortBy:
            if sort_by.name == value.lower():
                return sort_by

        raise LookupError("Unknown movie sort by option for value: {value}".format(value=value))