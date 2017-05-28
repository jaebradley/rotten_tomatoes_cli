import emoji


class RatingFormatter:
    NONE_EMOJI = emoji.emojize(":no_entry_sign:", use_aliases=True)
    ONE_HUNNID_EMOJI = emoji.emojize(":100:", use_aliases=True)
    SHIT_EMOJI = emoji.emojize(":shit:", use_aliases=True)
    GRIMACE_EMOJI = emoji.emojize(":grimace:", use_aliases=True)
    OK_EMOJI = emoji.emojize(":ok_hand:", use_aliases=True)
    GOOD_EMOJI = emoji.emojize(":+1:", use_aliases=True)
    GREAT_EMOJI = emoji.emojize(":sparkles:", use_aliases=True)

    def __init__(self):
        pass

    def format(self, rating):
        rating_emoji = self.rating_emoji(rating=rating)

        if rating is None:
            return "{rating_emoji}  N/A {rating_emoji} ".format(rating_emoji=rating_emoji)

        return "{rating_emoji}  {rating}% {rating_emoji} ".format(rating_emoji=rating_emoji, rating=rating)

    def rating_emoji(self, rating):
        if rating is None:
            return RatingFormatter.NONE_EMOJI

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