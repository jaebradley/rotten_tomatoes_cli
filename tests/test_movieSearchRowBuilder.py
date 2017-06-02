from unittest import TestCase

from mock import patch, Mock

from tables.rows.builders import MovieSearchRowBuilder


class MockMovie:
    def __init__(self, name, rotten_tomatoes_score, year, cast):
        self.name = name
        self.rotten_tomatoes_score = rotten_tomatoes_score
        self.year = year
        self.cast = cast


class TestMovieSearchRowBuilderCast(TestCase):
    row_builder = MovieSearchRowBuilder()

    @patch("tables.rows.builders.convert_to_ascii")
    def test_cast(self, mock_ascii_conversion):
        mock_ascii_conversion.return_value = "converted to ascii"
        cast = ["actor1", "actor2"]
        expected = "converted to ascii\nconverted to ascii"
        self.assertEqual(expected, self.row_builder.cast(cast=cast))
        mock_ascii_conversion.assert_any_call(text="actor1")
        mock_ascii_conversion.assert_any_call(text="actor2")


class TestMovieSearchRowBuilderName(TestCase):
    row_builder = MovieSearchRowBuilder()

    @patch("tables.rows.builders.convert_to_ascii")
    @patch("tables.rows.builders.colored")
    @patch("tables.rows.builders.wrap")
    def test_name(self, mock_wrap, mock_colored, mock_ascii_conversion):
        name_parts = ["jae", "baebae"]
        mock_ascii_conversion.return_value = "converted to ascii"
        mock_colored.return_value = "colored"
        mock_wrap.return_value = name_parts
        expected = "colored\ncolored"

        self.assertEqual(expected, self.row_builder.name(name="name"))
        mock_ascii_conversion.assert_called_once_with(text="name")
        mock_wrap.assert_called_once_with(text="converted to ascii", width=30)
        mock_colored.assert_any_call("jae", attrs=["bold"])
        mock_colored.assert_any_call("baebae", attrs=["bold"])


class TestMovieSearchRowBuilderBuild(TestCase):
    row_builder = MovieSearchRowBuilder()

    def test_build(self):
        year = "year"
        name = "name"
        cast = "cast"
        rotten_tomatoes_score = "rotten tomatoes score"
        movie = MockMovie(name=name, rotten_tomatoes_score=rotten_tomatoes_score, year=year, cast=cast)
        rating_formatter = "rating formatter"
        self.row_builder.name = Mock("name")
        self.row_builder.name.return_value = name
        self.row_builder.rating_formatter.format = Mock("rating_formatter")
        self.row_builder.rating_formatter.format.return_value = rating_formatter
        self.row_builder.cast = Mock("cast")
        self.row_builder.cast.return_value = cast
        expected = [name, rating_formatter, year, cast]
        self.assertEqual(expected, self.row_builder.build(movie=movie))
        self.row_builder.name.assert_called_once_with(name=name)
        self.row_builder.rating_formatter.format.assert_called_once_with(rating=rotten_tomatoes_score)
        self.row_builder.cast.assert_called_once_with(cast=cast)
