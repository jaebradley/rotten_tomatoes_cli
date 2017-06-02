from unittest import TestCase

from mock import patch, Mock

from tables.rows.builders import BrowseMovieRowBuilder


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
