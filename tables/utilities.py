from termcolor import colored


class RatingFormatter:
    def __init__(self):
        pass

    def format(self, rating):
        if rating is None:
            return "N/A"

        return colored(text="{rating}% ".format(rating=rating), color=self.rating_color(rating=rating))

    def rating_color(self, rating):
        if rating < 25:
            return "grey"

        elif rating < 50:
            return "green"

        elif rating < 75:
            return "white"

        elif rating < 90:
            return "yellow"

        else:
            return "red"