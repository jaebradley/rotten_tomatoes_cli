from unittest import TestCase

from mock import Mock, patch

from data.services import RottenTomatoesTvShowsBrowser


class TestRottenTomatoesTvShowsBrowser(TestCase):
    browser = RottenTomatoesTvShowsBrowser()

    @patch("rotten_tomatoes_client.RottenTomatoesClient.browse_tv_shows")
    def test_browse(self, mocked_client_browse_tv_shows):
        results = {"results": "jaebaebae"}
        category = "category"
        tv_shows = "tv shows"
        self.browser.tv_shows_parser.parse = Mock("mock_parse")
        self.browser.tv_shows_parser.parse.return_value = tv_shows
        mocked_client_browse_tv_shows.return_value = results

        outcome = self.browser.browse(category=category)

        mocked_client_browse_tv_shows.assert_called_once_with(category=category)
        self.browser.tv_shows_parser.parse.assert_called_once_with(tv_show_results="jaebaebae")
        self.assertEqual(outcome, tv_shows)
