from unittest import TestCase

from mock import Mock, patch


from tables.utilities import RottenTomatoesScoreFormatter


class TestRatingColor(TestCase):
    formatter = RottenTomatoesScoreFormatter()

    def test_should_return_cyan_for_rating_less_than_25(self):
        self.assertEqual("cyan", self.formatter.rating_color(rating=24))

    def test_should_return_green_for_rating_that_is_25(self):
        self.assertEqual("green", self.formatter.rating_color(rating=25))

    def test_should_return_green_for_rating_that_is_between_25_and_50(self):
        self.assertEqual("green", self.formatter.rating_color(rating=30))

    def test_should_return_white_for_rating_that_is_50(self):
        self.assertEqual("white", self.formatter.rating_color(rating=50))

    def test_should_return_white_for_rating_that_is_between_50_and_75(self):
        self.assertEqual("white", self.formatter.rating_color(rating=60))

    def test_should_return_yellow_for_rating_that_is_75(self):
        self.assertEqual("yellow", self.formatter.rating_color(rating=75))

    def test_should_return_yellow_for_rating_between_75_and_90(self):
        self.assertEqual("yellow", self.formatter.rating_color(rating=80))

    def test_should_return_red_for_rating_that_is_90(self):
        self.assertEqual("red", self.formatter.rating_color(rating=90))

    def test_should_return_red_for_rating_greater_than_90(self):
        self.assertEqual("red", self.formatter.rating_color(rating=100))


class TestFormatting(TestCase):
    formatter = RottenTomatoesScoreFormatter()

    def test_should_return_na_for_none_rating(self):
        self.assertEqual("N/A", self.formatter.format(rating=None))

    @patch("tables.utilities.colored")
    def test_should_return_formatted_rating(self, mock_colored):
        rating = "rating"
        rating_color = "rating color"
        colored = "colored"
        self.formatter.rating_color = Mock("rating color")
        self.formatter.rating_color.return_value = rating_color
        mock_colored.return_value = colored
        self.assertEqual(colored, self.formatter.format(rating=rating))
        self.formatter.rating_color.assert_called_once_with(rating=rating)
        mock_colored.assert_called_once_with(text="rating% ", color=rating_color)