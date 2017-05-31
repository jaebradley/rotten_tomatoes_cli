from unittest import TestCase

from mock import Mock

from data.parsers import TvShowSearchResultsParser
from data import TvShowSearchResult


class TestTvShowSearchResultsParser(TestCase):
    parser = TvShowSearchResultsParser()

    def test_returns_none_when_rotten_tomatoes_score_does_not_exist(self):
        self.assertIsNone(self.parser.rotten_tomatoes_score(result={}))

    def test_returns_rotten_tomatoes_score_when_it_exists(self):
        rotten_tomatoes_score = "jaebaebae"
        result = {"meterScore": rotten_tomatoes_score}
        self.assertEqual(self.parser.rotten_tomatoes_score(result=result), rotten_tomatoes_score)

    def test_returns_none_when_year_is_zero(self):
        self.assertIsNone(self.parser.year(year=0))

    def test_returns_year_when_year_is_non_zero(self):
        year = "jaebaebae"
        self.assertEqual(self.parser.year(year=year), year)


class TestTvShowSearchResultsParsing(TestCase):
    parser = TvShowSearchResultsParser()

    def test_parsing_list_of_results(self):
        self.parser.year = Mock("parse_year")
        self.parser.year.return_value = "jae"
        self.parser.rotten_tomatoes_score = Mock("parse_score")
        self.parser.rotten_tomatoes_score.return_value = "baebae"
        tv_show_result = {
            "title": "title",
            "startYear": "startYear",
            "endYear": "endYear"
        }
        tv_show_results = [tv_show_result, tv_show_result]
        expected_tv_show_result = TvShowSearchResult(name="title", start_year="startYear",
                                                     end_year="jae", rotten_tomatoes_score="baebae")
        expected = [expected_tv_show_result, expected_tv_show_result]
        self.assertEqual(self.parser.parse(tv_show_results=tv_show_results), expected)
