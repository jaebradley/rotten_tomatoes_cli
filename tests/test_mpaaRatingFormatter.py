from unittest import TestCase

from mock import patch, Mock


from tables.utilities import MpaaRatingFormatter


class TestRatingColor(TestCase):
    formatter = MpaaRatingFormatter()

    def test_should_return_white_for_not_rated(self):
        self.assertEqual(self.formatter.rating_color(rating="NR"), "white")

    def test_should_return_green_for_g_rated(self):
        self.assertEqual(self.formatter.rating_color(rating="G"), "green")

    def test_should_return_cyan_for_pg_rated(self):
        self.assertEqual(self.formatter.rating_color(rating="PG"), "cyan")

    def test_should_return_yellow_for_pg_13_rated(self):
        self.assertEqual(self.formatter.rating_color(rating="PG13"), "yellow")

    def test_should_return_red_for_r_rated(self):
        self.assertEqual(self.formatter.rating_color(rating="R"), "red")

    def test_should_return_magenta_for_unknown_rating(self):
        self.assertEqual(self.formatter.rating_color(rating="foo"), "magenta")


class TestFormatter(TestCase):
    formatter = MpaaRatingFormatter()

    @patch("tables.utilities.colored")
    def test_should_format(self, mock_colored):
        rating = "rating"
        colored = "colored"
        rating_color = "rating color"
        mock_colored.return_value = colored
        self.formatter.rating_color = Mock("mock rating color")
        self.formatter.rating_color.return_value = rating_color
        self.assertEqual(colored, self.formatter.format(rating=rating))
        self.formatter.rating_color.assert_called_once_with(rating=rating)
        mock_colored.assert_called_once_with(text=rating, color=rating_color)