from unittest import TestCase

from mock import Mock, patch

from data.services import RottenTomatoesMoviesBrowser


class TestRottenTomatoesMoviesBrowser(TestCase):
    browser = RottenTomatoesMoviesBrowser()

    @patch("rotten_tomatoes_client.RottenTomatoesClient.browse_movies")
    def test_browse(self, mocked_client_browse_movies):
        results = {"results": "jaebaebae"}
        mocked_client_browse_movies.return_value = results
        self.browser.parser.parse = Mock("mock_parser")
        self.browser.parser.parse.return_value = "jaebaebae"

        movies = self.browser.browse(query="query")

        self.browser.parser.parse.assert_called_once_with(movie_results="jaebaebae")
        mocked_client_browse_movies.assert_called_once_with(query="query")
        self.assertEqual("jaebaebae", movies)
