import logging
from unittest import TestCase

from data import BrowseTvShowResult
from tables.builders import BrowseTvShowTableBuilder
from tables.rows.builders import BrowseTvShowRowBuilder

logging.basicConfig(level=logging.DEBUG)


class IntegrationTest(TestCase):
    table_builder = BrowseTvShowTableBuilder(BrowseTvShowRowBuilder())

    def test_should_return_table_output(self):
        result = BrowseTvShowResult(title="title", rotten_tomatoes_score=100)
        another_result = BrowseTvShowResult(title="another title", rotten_tomatoes_score=0)
        tv_shows = [result, another_result]
        expected = """\x1b(0lqqqqqqqqqqqqqqqwqqqqqqqk\x1b(B\n\x1b(0x\x1b(B \x1b[4m\x1b[1mTV Show\x1b[0m       \x1b(0x\x1b(B \x1b[4m\x1b[1mScore\x1b[0m \x1b(0x\x1b(B\n\x1b(0tqqqqqqqqqqqqqqqnqqqqqqqu\x1b(B\n\x1b(0x\x1b(B title         \x1b(0x\x1b(B \x1b[31m100% \x1b[0m \x1b(0x\x1b(B\n\x1b(0tqqqqqqqqqqqqqqqnqqqqqqqu\x1b(B\n\x1b(0x\x1b(B another title \x1b(0x\x1b(B \x1b[36m0% \x1b[0m   \x1b(0x\x1b(B\n\x1b(0mqqqqqqqqqqqqqqqvqqqqqqqj\x1b(B"""
        output = self.table_builder.build(tv_shows)

        logging.debug("Expected TV Shows Browse Table:\n{expected}".format(expected=expected))
        logging.debug("Actual TV Shows Browse Table:\n{output}".format(output=output))

        self.assertEqual(output, expected)
