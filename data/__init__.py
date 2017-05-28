class MovieSearchResult:
    def __init__(self, name, year, rotten_tomatoes_score, cast):
        self.name = name
        self.year = year
        self.rotten_tomatoes_score = rotten_tomatoes_score
        self.cast = cast


class TvShowSearchResult:
    def __init__(self, name, start_year, end_year, rotten_tomatoes_score):
        self.name = name
        self.start_year = start_year
        self.end_year = end_year
        self.rotten_tomatoes_score = rotten_tomatoes_score


class SearchResult:
    def __init__(self, movies, tv_shows):
        self.movies = movies
        self.tv_shows = tv_shows
