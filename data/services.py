from rotten_tomatoes_client import RottenTomatoesClient

from data import SearchResult
from data.parsers import TvShowSearchResultsParser, MovieSearchResultsParser, TvShowBrowseResultsParser, MovieBrowseResultsParser


class RottenTomatoesSearcher:

    def __init__(self):
        self.tv_shows_parser = TvShowSearchResultsParser()
        self.movies_parser = MovieSearchResultsParser()

    def search(self, term):
        results = RottenTomatoesClient.search(term=term)
        return SearchResult(movies=self.movies_parser.parse(movie_results=results["movies"]),
                            tv_shows=self.tv_shows_parser.parse(tv_show_results=results["tvSeries"]))


class RottenTomatoesTvShowsBrowser:
    def __init__(self):
        self.tv_shows_parser = TvShowBrowseResultsParser()

    def browse(self, category):
        results = RottenTomatoesClient.browse_tv_shows(category=category)
        return self.tv_shows_parser.parse(tv_show_results=results["results"])


class RottenTomatoesMoviesBrowser:
    def __init__(self):
        self.parser = MovieBrowseResultsParser()

    def browse(self, query):
        results = RottenTomatoesClient.browse_movies(query=query)
        return self.parser.parse(movie_results=results["results"])
