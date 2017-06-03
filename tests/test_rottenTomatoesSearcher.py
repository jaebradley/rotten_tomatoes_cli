from unittest import TestCase

from mock import Mock, patch

from data import SearchResult
from data.services import RottenTomatoesSearcher


class TestRottenTomatoesSearcher(TestCase):
    searcher = RottenTomatoesSearcher()

    @patch("rotten_tomatoes_client.RottenTomatoesClient.search")
    def test_search(self, mocked_search):
        term = "term"
        tv_show_results = "tv show results"
        movie_results = "movie results"
        results = {"movies": movie_results, "tvSeries": tv_show_results}
        movies = "movies"
        tv_shows = "tv shows"
        self.searcher.tv_shows_parser.parse = Mock("parse_tv_shows")
        self.searcher.tv_shows_parser.parse.return_value = tv_shows
        self.searcher.movies_parser.parse = Mock("parse_movies")
        self.searcher.movies_parser.parse.return_value = movies
        mocked_search.return_value = results
        expected = SearchResult(movies=movies, tv_shows=tv_shows)

        search_result = self.searcher.search(term=term)

        mocked_search.assert_called_once_with(term=term)
        self.searcher.tv_shows_parser.parse.assert_called_once_with(tv_show_results=tv_show_results)
        self.searcher.movies_parser.parse.assert_called_once_with(movie_results=movie_results)
        self.assertEqual(expected, search_result)
