from unittest import TestCase

from mock import Mock

from data.parsers import MovieBrowseResultsParser
from data import BrowseMovieResult


class TestMovieBrowseResultsRottenTomatoesScoreParsing(TestCase):
    parser = MovieBrowseResultsParser()

    def test_none_when_no_score_exists(self):
        self.assertIsNone(self.parser.rotten_tomatoes_score(result={}))

    def test_returns_score_when_exists(self):
        score = "jaebaebae"
        result = {"tomatoScore": score}
        self.assertEqual(score, self.parser.rotten_tomatoes_score(result=result))


class TestMovieBrowseResultsDvdReleaseDateParsing(TestCase):
    parser = MovieBrowseResultsParser()

    def test_none_when_no_dvd_release_date_exists(self):
        self.assertIsNone(self.parser.dvd_release_date(result={}))

    def test_returns_when_no_dvd_release_date_exists(self):
        dvd_release_date = "jaebaebae"
        result = {"dvdReleaseDate": dvd_release_date}
        self.assertEqual(dvd_release_date, self.parser.dvd_release_date(result=result))


class TestMovieBrowseResultsTheaterReleaseDateParsing(TestCase):
    parser = MovieBrowseResultsParser()

    def test_none_when_no_theater_release_date_exists(self):
        self.assertIsNone(self.parser.theater_release_date(result={}))

    def test_returns_when_no_theater_release_date_exists(self):
        theater_release_date = "jaebaebae"
        result = {"theaterReleaseDate": theater_release_date}
        self.assertEqual(theater_release_date, self.parser.theater_release_date(result=result))


class TestMovieBrowseResultsRuntimeParsing(TestCase):
    parser = MovieBrowseResultsParser()

    def test_none_when_no_runtime_exists(self):
        self.assertIsNone(self.parser.runtime(result={}))

    def test_returns_when_no_runtime_exists(self):
        runtime = "jaebaebae"
        result = {"runtime": runtime}
        self.assertEqual(runtime, self.parser.runtime(result=result))


class TestMovieBrowseResultsParsing(TestCase):
    parser = MovieBrowseResultsParser()

    def test_parsing(self):
        title = "title"
        synopsis = "synopsis"
        mpaa_rating = "mpaa rating"
        actors = "actors"
        rotten_tomatoes_score = "rotten tomatoes score"
        dvd_release_date = "dvd release date"
        theater_release_date = "theater release date"
        runtime = "runtime"
        self.parser.rotten_tomatoes_score = Mock("parse_rotten_tomatoes_score")
        self.parser.rotten_tomatoes_score.return_value = rotten_tomatoes_score
        self.parser.dvd_release_date = Mock("parse_dvd_release_date")
        self.parser.dvd_release_date.return_value = dvd_release_date
        self.parser.theater_release_date = Mock("parse_theater_release_date")
        self.parser.theater_release_date.return_value = theater_release_date
        self.parser.runtime = Mock("parse_runtime")
        self.parser.runtime.return_value = runtime
        movie_result = {
            "title": title,
            "synopsis": synopsis,
            "mpaaRating": mpaa_rating,
            "actors": actors
        }
        movie_results = [movie_result, movie_result]
        expected_movie_result = BrowseMovieResult(title=title, rotten_tomatoes_score=rotten_tomatoes_score,
                                                  synopsis=synopsis, runtime=runtime,
                                                  theater_release_date=theater_release_date,
                                                  dvd_release_date=dvd_release_date, mpaa_rating=mpaa_rating,
                                                  actors=actors)
        expected = [expected_movie_result, expected_movie_result]
        self.assertEqual(expected, self.parser.parse(movie_results=movie_results))

