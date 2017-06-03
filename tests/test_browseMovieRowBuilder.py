from unittest import TestCase

from mock import patch, Mock

from tables.rows.builders import BrowseMovieRowBuilder


class MockMovie:
    def __init__(self, theater_release_date=None, dvd_release_date=None, rotten_tomatoes_score=None, mpaa_rating=None, runtime=None, actors=None):
        self.theater_release_date = theater_release_date
        self.dvd_release_date = dvd_release_date
        self.rotten_tomatoes_score = rotten_tomatoes_score
        self.mpaa_rating = mpaa_rating
        self.runtime = runtime
        self.actors = actors


class TestName(TestCase):
    row_builder = BrowseMovieRowBuilder()

    @patch("tables.rows.builders.convert_to_ascii")
    @patch("tables.rows.builders.colored")
    @patch("tables.rows.builders.wrap")
    def test_title(self, mock_wrap, mock_colored, mock_ascii_conversion):
        title_parts = ["jae", "baebae"]
        mock_ascii_conversion.return_value = "converted to ascii"
        mock_colored.return_value = "colored"
        mock_wrap.return_value = title_parts
        expected = "colored\ncolored"

        self.assertEqual(expected, self.row_builder.title(title="title"))
        mock_ascii_conversion.assert_called_once_with(text="title")
        mock_wrap.assert_called_once_with(text="converted to ascii", width=50)
        mock_colored.assert_any_call("jae", attrs=["bold", "underline"])
        mock_colored.assert_any_call("baebae", attrs=["bold", "underline"])


class TestSynopsis(TestCase):
    row_builder = BrowseMovieRowBuilder()

    @patch("tables.rows.builders.clean_html")
    @patch("tables.rows.builders.convert_to_ascii")
    @patch("tables.rows.builders.wrap")
    def test_synopsis(self, mock_wrap, mock_ascii_conversion, mock_clean_html):
        synopsis_parts = ["jae", "baebae"]
        mock_clean_html.return_value = "clean html"
        mock_ascii_conversion.return_value = "converted to ascii"
        mock_wrap.return_value = synopsis_parts
        expected = "jae\nbaebae"

        self.assertEqual(expected, self.row_builder.synopsis(synopsis="synopsis"))

        mock_clean_html.assert_called_once_with(raw_html="synopsis")
        mock_ascii_conversion.assert_called_once_with(text="clean html")
        mock_wrap.assert_called_once_with(text="converted to ascii", width=50)


class TestRuntime(TestCase):
    row_builder = BrowseMovieRowBuilder()

    def test_when_none(self):
        self.assertEqual(self.row_builder.runtime(runtime=None), "N/A")

    def test_when_not_none(self):
        runtime = "runtime"
        self.assertEqual(self.row_builder.runtime(runtime=runtime), runtime)


class TestActors(TestCase):
    row_builder = BrowseMovieRowBuilder()

    @patch("tables.rows.builders.convert_to_ascii")
    def test_actors(self, mock_ascii_conversion):
        mock_ascii_conversion.return_value = "converted to ascii"
        actors = ["actor1", "actor2"]
        expected = "converted to ascii\nconverted to ascii"
        self.assertEqual(expected, self.row_builder.actors(actors=actors))
        mock_ascii_conversion.assert_any_call(text="actor1")
        mock_ascii_conversion.assert_any_call(text="actor2")


class TestReleaseDates(TestCase):
    row_builder = BrowseMovieRowBuilder()

    def test_should_return_movie_theater_release_date(self):
        theater_release_date = "theater release date"
        movie = MockMovie(theater_release_date=theater_release_date, dvd_release_date=None)
        self.assertEqual("theater release date (Theaters)", self.row_builder.release_dates(movie=movie))

    def test_should_return_dvd_release_date(self):
        dvd_release_date = "dvd release date"
        movie = MockMovie(theater_release_date=None, dvd_release_date=dvd_release_date)
        self.assertEqual("dvd release date (DVD)", self.row_builder.release_dates(movie=movie))


class TestDetails(TestCase):
    row_builder = BrowseMovieRowBuilder()

    @patch("tables.rows.builders.formatted_header")
    def test_should_return_details(self, mocked_formatted_header):
        score = "score"
        rating = "rating"
        runtime = "runtime"
        release = "release"
        actors = "actors"
        movie = MockMovie(rotten_tomatoes_score=score, mpaa_rating=rating, runtime=runtime, actors=actors)
        mocked_formatted_header.return_value = "formatted header"
        self.row_builder.rotten_tomatoes_score_formatter.format = Mock("rotten tomatoes score formatter")
        self.row_builder.rotten_tomatoes_score_formatter.format.return_value = score
        self.row_builder.mpaa_rating_formatter.format = Mock("mpaa rating formatter")
        self.row_builder.mpaa_rating_formatter.format.return_value = rating
        self.row_builder.runtime = Mock("runtime")
        self.row_builder.runtime.return_value = runtime
        self.row_builder.release_dates = Mock("release dates")
        self.row_builder.release_dates.return_value = release
        self.row_builder.actors = Mock("actors")
        self.row_builder.actors.return_value = actors

        expected = "formatted header\nscore\n\nformatted header\nrating\n\nformatted header\nruntime\n\nformatted header\nrelease\n\nformatted header\nactors"
        self.assertEqual(expected, self.row_builder.details(movie=movie))
        self.row_builder.rotten_tomatoes_score_formatter.format.assert_called_once_with(rating=score)
        self.row_builder.mpaa_rating_formatter.format.assert_called_once_with(rating=rating)
        self.row_builder.runtime.assert_called_once_with(runtime=runtime)
        self.row_builder.release_dates.assert_called_once_with(movie=movie)
        self.row_builder.actors.assert_called_once_with(actors=actors)
        mocked_formatted_header.assert_any_call(text="Score")
        mocked_formatted_header.assert_any_call(text="Rating")
        mocked_formatted_header.assert_any_call(text="Runtime")
        mocked_formatted_header.assert_any_call(text="Release")
        mocked_formatted_header.assert_any_call(text="Actors")

