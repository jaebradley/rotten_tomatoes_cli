from unittest import TestCase

from mock import Mock

from data import BrowseTvShowResult
from data.parsers import TvShowBrowseResultsParser


class TestTvShowBrowseResultsRottenTomatoesParsing(TestCase):
    parser = TvShowBrowseResultsParser()

    def test_returns_none_when_no_score_exists(self):
        self.assertIsNone(self.parser.rotten_tomatoes_score(result={}))

    def test_returns_value_when_no_score_exists(self):
        tomato_score = "jaebaebae"
        result = {"tomatoScore": tomato_score}
        self.assertEqual(tomato_score, self.parser.rotten_tomatoes_score(result=result))


class TestTvShowBrowseResultsParsing(TestCase):
    parser = TvShowBrowseResultsParser()

    def test_parse(self):
        title = "jae"
        rotten_tomatoes_score = "baebae"
        self.parser.rotten_tomatoes_score = Mock("parse_rotten_tomatoes_score")
        self.parser.rotten_tomatoes_score.return_value = rotten_tomatoes_score
        tv_show_result = {"title": title}
        tv_show_results = [tv_show_result, tv_show_result]
        expected_tv_show_result = BrowseTvShowResult(title=title, rotten_tomatoes_score=rotten_tomatoes_score)
        expected = [expected_tv_show_result, expected_tv_show_result]
        self.assertEqual(expected, self.parser.parse(tv_show_results=tv_show_results))
