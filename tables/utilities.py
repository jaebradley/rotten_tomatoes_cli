from termcolor import colored
import re


class RatingFormatter:
    def __init__(self):
        pass

    def format(self, rating):
        if rating is None:
            return "N/A"

        return colored(text="{rating}% ".format(rating=rating), color=self.rating_color(rating=rating))

    def rating_color(self, rating):
        if rating < 25:
            return "cyan"

        elif rating < 50:
            return "green"

        elif rating < 75:
            return "white"

        elif rating < 90:
            return "yellow"

        else:
            return "red"


def as_ascii(text):
    return text.encode("ascii", "ignore").decode("ascii")


def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    clean_text = re.sub(cleanr, '', raw_html)
    return clean_text
