import emoji


class RatingFormatter:
    ONE_HUNNID_EMOJI = emoji.emojize(":100:")
    SHIT_EMOJI = emoji.emojize(":shit:")
    GRIMACE_EMOJI = emoji.emojize(":grimace:")
    OK_EMOJI = emoji.emojize(":ok_hand:")
    GOOD_EMOJI = emoji.emojize(":+1:")
    GREAT_EMOJI = emoji.emojize(":sparkles:")

    def __init__(self):
        pass

    def format(self, rating):
        return "{rating_emoji} {rating}% {rating_emoji}"\
            .format(rating_emoji=self.rating_emoji(rating=rating), rating=rating)

    def rating_emoji(self, rating):
        if rating == 100:
            return RatingFormatter.ONE_HUNNID_EMOJI

        elif rating < 25:
            return RatingFormatter.SHIT_EMOJI

        elif rating < 50:
            return RatingFormatter.GRIMACE_EMOJI

        elif rating < 75:
            return RatingFormatter.OK_EMOJI

        elif rating < 90:
            return RatingFormatter.GOOD_EMOJI

        else:
            return RatingFormatter.GREAT_EMOJI