import logging
from unittest import TestCase

from data import TvShowSearchResult
from tables.builders import TvShowSearchTableBuilder
from tables.rows.builders import TvShowSearchRowBuilder

logging.basicConfig(level=logging.DEBUG)


class IntegrationTest(TestCase):
    table_builder = TvShowSearchTableBuilder(TvShowSearchRowBuilder())

    def test_should_return_table_output(self):
        result = TvShowSearchResult(name="name",
                                    start_year="start year",
                                    end_year="end year",
                                    rotten_tomatoes_score=1)
        another_result = TvShowSearchResult(name="another name",
                                            start_year="another start year",
                                            end_year=None,
                                            rotten_tomatoes_score=100)
        tv_shows = [result, another_result]

        expected = """(0lqqqqqqqqqqqqqqwqqqqqqqwqqqqqqqqqqqqqqqqqqqqqk(B
(0x(B [4m[1mTV Show[0m      (0x(B [4m[1mScore[0m (0x(B [4m[1mYears[0m               (0x(B
(0tqqqqqqqqqqqqqqnqqqqqqqnqqqqqqqqqqqqqqqqqqqqqu(B
(0x(B [1manother name[0m (0x(B [31m100% [0m (0x(B another start year- (0x(B
(0tqqqqqqqqqqqqqqnqqqqqqqnqqqqqqqqqqqqqqqqqqqqqu(B
(0x(B [1mname[0m         (0x(B [36m1% [0m   (0x(B start year-end year (0x(B
(0mqqqqqqqqqqqqqqvqqqqqqqvqqqqqqqqqqqqqqqqqqqqqj(B"""
        output = self.table_builder.build(tv_shows)

        logging.debug("Expected TV Show Search Table:\n{expected}".format(expected=expected))
        logging.debug("Actual TV Show Search Table:\n{output}".format(output=output))

        self.assertEqual(output, expected)

