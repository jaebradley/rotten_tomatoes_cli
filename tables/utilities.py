import emoji


class RatingFormatter:

    def __init__(self):
        pass

    def format(self, rating):
        return "{rating_emoji} {rating}% {rating_emoji}"\
            .format(rating_emoji=self.rating_emoji(rating=rating), rating=rating)

    def rating_emoji(self, rating):
        if rating == 100:
            return emoji.emojize(":100:")

        elif rating < 25:
            return emoji.emojize(":shit:")

        elif rating < 50:
            return emoji.emojize(":grimace:")

        elif rating < 75:
            return emoji.emojize(":ok_hand:")

        elif rating < 90:
            return emoji.emojize(":+1:")

        else:
            return emoji.emojize(":sparkles:")