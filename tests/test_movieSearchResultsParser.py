from unittest import TestCase

from mock import Mock

from data import MovieSearchResult
from data.parsers import MovieSearchResultsParser


class TestMovieSearchResultsCastParsing(TestCase):
    parser = MovieSearchResultsParser()

    def test_cast(self):
        cast_member = {"name": "jae"}
        another_cast_member = {"name": "baebae"}
        cast = [cast_member, another_cast_member]
        expected = ["jae", "baebae"]
        self.assertEqual(expected, self.parser.cast(cast=cast))


class TestMovieSearchResultsRottenTomatoesScoreParsing(TestCase):
    parser = MovieSearchResultsParser()

    def test_rotten_tomatoes_score_when_none(self):
        self.assertIsNone(self.parser.rotten_tomatoes_score(result={}))

    def test_rotten_tomatoes_score_when_exists(self):
        rotten_tomatoes_score = "jaebaebae"
        result = {"meterScore": rotten_tomatoes_score}
        self.assertEqual(rotten_tomatoes_score, self.parser.rotten_tomatoes_score(result=result))


class TestMovieSearchResultsParser(TestCase):
    parser = MovieSearchResultsParser()

    def test_parse(self):
        name = "name"
        year = "year"
        cast = "jae"
        rotten_tomatoes_score = "baebae"
        self.parser.cast = Mock("parse_cast")
        self.parser.cast.return_value = cast
        self.parser.rotten_tomatoes_score = Mock("parse_rotten_tomatoes_score")
        self.parser.rotten_tomatoes_score.return_value = rotten_tomatoes_score
        movie_result = {
            "name": name,
            "year": year,
            "castItems": "foo"
        }
        movie_results = [movie_result, movie_result]
        expected_movie_result = MovieSearchResult(name=name, year=year, rotten_tomatoes_score=rotten_tomatoes_score,
                                                  cast=cast)
        expected = [expected_movie_result, expected_movie_result]
        self.assertEqual(expected, self.parser.parse(movie_results=movie_results))
