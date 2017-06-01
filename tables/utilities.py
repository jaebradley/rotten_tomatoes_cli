import re

from termcolor import colored


class RottenTomatoesScoreFormatter:
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


class MpaaRatingFormatter:
    def __init__(self):
        pass

    def format(self, rating):
        return colored(text=rating, color=self.rating_color(rating=rating))

    def rating_color(self, rating):
        if rating == "NR":
            return "white"

        elif rating == "G":
            return "green"

        elif rating == "PG":
            return "cyan"

        elif rating == "PG13":
            return "yellow"

        elif rating == "R":
            return "red"

        else:
            return "magenta"


def convert_to_ascii(text):
    return text.encode("ascii", "ignore").decode("ascii")


def clean_html(raw_html):
    clean = re.compile("<.*?>")
    clean_text = re.sub(clean, "", raw_html)
    return clean_text


def formatted_header(text):
    return colored(text=convert_to_ascii(text=text), attrs=["bold", "underline"])
