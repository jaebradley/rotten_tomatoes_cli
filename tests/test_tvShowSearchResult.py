from unittest import TestCase

from data import TvShowSearchResult


class TestTvShowSearchResult(TestCase):
    name = "name"
    start_year = "start_year"
    end_year = "end_year"
    rotten_tomatoes_score = "rotten_tomatoes_score"
    result = TvShowSearchResult(name=name, start_year=start_year, end_year=end_year,
                                rotten_tomatoes_score=rotten_tomatoes_score)

    def test_equals(self):
        another_result = TvShowSearchResult(name=self.name, start_year=self.start_year, end_year=self.end_year,
                                            rotten_tomatoes_score=self.rotten_tomatoes_score)
        self.assertEqual(self.result, another_result)

    def test_equals_throws_not_implemented(self):
        self.assertEqual(NotImplemented, self.result.__eq__("foo"))

    def test_not_equals(self):
        another_result = TvShowSearchResult(name="jaebaebae", start_year=self.start_year, end_year=self.end_year,
                                            rotten_tomatoes_score=self.rotten_tomatoes_score)
        self.assertNotEqual(self.result, another_result)

    def test_not_equals_throws_not_implemented(self):
        self.assertEqual(NotImplemented, self.result.__ne__("foo"))

    def test_hash(self):
        self.assertEqual(self.result.__hash__(), hash(tuple(sorted(self.result.__dict__.items()))))
