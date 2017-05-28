from unittest import TestCase
from mock import patch

from tables.utilities import RatingFormatter


class TestRatingFormatter(TestCase):
    formatter = RatingFormatter()

    def test_rating_emoji_when_rating_is_100(self):
        self.assertEqual(self.formatter.rating_emoji(rating=100), RatingFormatter.ONE_HUNNID_EMOJI)

    def test_rating_emoji_when_rating_lt_25(self):
        self.assertEqual(self.formatter.rating_emoji(rating=10), RatingFormatter.SHIT_EMOJI)

    def test_rating_emoji_when_rating_gte_25_and_lt_50(self):
        self.assertEqual(self.formatter.rating_emoji(rating=25), RatingFormatter.GRIMACE_EMOJI)

    def test_rating_emoji_when_rating_gte_50_and_lt_75(self):
        self.assertEqual(self.formatter.rating_emoji(rating=50), RatingFormatter.OK_EMOJI)

    def test_rating_emoji_when_rating_gte_75_and_let_90(self):
        self.assertEqual(self.formatter.rating_emoji(rating=75), RatingFormatter.GOOD_EMOJI)

    def test_rating_emoji_when_rating_gt_90(self):
        self.assertEqual(self.formatter.rating_emoji(rating=91), RatingFormatter.GREAT_EMOJI)

    def test_format(self):
        with patch.object(self.formatter, "rating_emoji") as mock_rating_emoji:
            mock_rating_emoji.return_value = "rating emoji"
            expected = "rating emoji rating% rating emoji"
            self.assertEqual(expected, self.formatter.format(rating="rating"))
            mock_rating_emoji.assert_called_once_with(rating="rating")
