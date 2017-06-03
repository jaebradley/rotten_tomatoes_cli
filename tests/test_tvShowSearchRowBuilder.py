from unittest import TestCase

from mock import patch, Mock

from tables.rows.builders import TvShowSearchRowBuilder


class MockTvShow:
    def __init__(self, name, rotten_tomatoes_score, start_year, end_year):
        self.name = name
        self.rotten_tomatoes_score = rotten_tomatoes_score
        self.start_year = start_year
        self.end_year = end_year


class TestName(TestCase):
    row_builder = TvShowSearchRowBuilder()

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


class TestFormatYears(TestCase):
    row_builder = TvShowSearchRowBuilder()
    start_year = "start year"

    def test_when_end_year_is_none(self):
        expected = "start year-"
        self.assertEqual(expected, self.row_builder.format_years(start_year=self.start_year, end_year=None))

    def test_when_end_year_is_defined(self):
        end_year = "end year"
        expected = "start year-end year"
        self.assertEqual(expected, self.row_builder.format_years(start_year=self.start_year, end_year=end_year))


class TestBuild(TestCase):
    row_builder = TvShowSearchRowBuilder()

    def test_build(self):
        name = "name"
        rotten_tomatoes_score = "rotten tomatoes score"
        start_year = "start year"
        end_year = "end year"
        tv_show = MockTvShow(name=name, rotten_tomatoes_score=rotten_tomatoes_score,
                             start_year=start_year, end_year=end_year)
        rating_formatter = "rating formatter"
        format_years = "format years"
        self.row_builder.name = Mock("name")
        self.row_builder.name.return_value = name
        self.row_builder.rating_formatter.format = Mock("format")
        self.row_builder.rating_formatter.format.return_value = rating_formatter
        self.row_builder.format_years = Mock("format years")
        self.row_builder.format_years.return_value = format_years

        expected = [name, rating_formatter, format_years]

        self.assertEqual(expected, self.row_builder.build(tv_show=tv_show))
        self.row_builder.name.assert_called_once_with(name=name)
        self.row_builder.rating_formatter.format.assert_called_once_with(rating=rotten_tomatoes_score)
        self.row_builder.format_years.assert_called_once_with(start_year=start_year, end_year=end_year)
