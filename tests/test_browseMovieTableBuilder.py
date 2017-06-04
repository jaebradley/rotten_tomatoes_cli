import logging
from unittest import TestCase

from data import BrowseMovieResult
from tables.builders import BrowseMovieTableBuilder
from tables.rows.builders import BrowseMovieRowBuilder

logging.basicConfig(level=logging.DEBUG)


class IntegrationTest(TestCase):
    table_builder = BrowseMovieTableBuilder(BrowseMovieRowBuilder())

    def test_should_return_table_output(self):
        result = BrowseMovieResult(title="title", rotten_tomatoes_score=100, synopsis="synopsis", runtime= "runtime", theater_release_date="Jun 5", dvd_release_date="Jun 6", mpaa_rating="R", actors=["jae", "baebae"])
        another_result = BrowseMovieResult(title="another title", rotten_tomatoes_score=1, synopsis="another synopsis", runtime="another runtime", theater_release_date="Jun 7", dvd_release_date="Jun 8", mpaa_rating="PG", actors=["another", "actor"])
        movies = [result, another_result]
        expected = """\x1b(0lqqqqqqqqqqqqqqqqqqwqqqqqqqqqqqqqqqqqqk\x1b(B\n\x1b(0x\x1b(B \x1b[4m\x1b[1m\x1b[0m                 \x1b(0x\x1b(B \x1b[4m\x1b[1mDetails\x1b[0m          \x1b(0x\x1b(B\n\x1b(0tqqqqqqqqqqqqqqqqqqnqqqqqqqqqqqqqqqqqqu\x1b(B\n\x1b(0x\x1b(B \x1b[4m\x1b[1mtitle\x1b[0m            \x1b(0x\x1b(B \x1b[4m\x1b[1mScore\x1b[0m            \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B \x1b[31m100% \x1b[0m            \x1b(0x\x1b(B\n\x1b(0x\x1b(B synopsis         \x1b(0x\x1b(B                  \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B \x1b[4m\x1b[1mRating\x1b[0m           \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B \x1b[31mR\x1b[0m                \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B                  \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B \x1b[4m\x1b[1mRuntime\x1b[0m          \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B runtime          \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B                  \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B \x1b[4m\x1b[1mRelease\x1b[0m          \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B Jun 5 (Theaters) \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B Jun 6 (DVD)      \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B                  \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B \x1b[4m\x1b[1mActors\x1b[0m           \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B jae              \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B baebae           \x1b(0x\x1b(B\n\x1b(0tqqqqqqqqqqqqqqqqqqnqqqqqqqqqqqqqqqqqqu\x1b(B\n\x1b(0x\x1b(B \x1b[4m\x1b[1manother title\x1b[0m    \x1b(0x\x1b(B \x1b[4m\x1b[1mScore\x1b[0m            \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B \x1b[36m1% \x1b[0m              \x1b(0x\x1b(B\n\x1b(0x\x1b(B another synopsis \x1b(0x\x1b(B                  \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B \x1b[4m\x1b[1mRating\x1b[0m           \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B \x1b[36mPG\x1b[0m               \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B                  \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B \x1b[4m\x1b[1mRuntime\x1b[0m          \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B another runtime  \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B                  \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B \x1b[4m\x1b[1mRelease\x1b[0m          \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B Jun 7 (Theaters) \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B Jun 8 (DVD)      \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B                  \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B \x1b[4m\x1b[1mActors\x1b[0m           \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B another          \x1b(0x\x1b(B\n\x1b(0x\x1b(B                  \x1b(0x\x1b(B actor            \x1b(0x\x1b(B\n\x1b(0mqqqqqqqqqqqqqqqqqqvqqqqqqqqqqqqqqqqqqj\x1b(B"""
        output = self.table_builder.build(movies)

        logging.debug("Expected Browse Movies Search Table:\n{expected}".format(expected=expected))
        logging.debug("Actual Browse Movies Search Table:\n{output}".format(output=output))

        self.assertEqual(output, expected)
