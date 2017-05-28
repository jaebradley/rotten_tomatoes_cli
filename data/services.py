from rotten_tomatoes_client import RottenTomatoesClient

from data import MovieSearchResult, SearchResult


class RottenTomatoesSearcher:

    def __init__(self):
        pass

    def search(self, term):
        results = RottenTomatoesClient.search(term=term)
        return SearchResult(movies=self.movies(movie_results=results["movies"]))

    def movies(self, movie_results):
        return [
            MovieSearchResult(name=movie_result["name"], year=movie_result["year"],
                              rotten_tomatoes_score=movie_result["score"],
                              cast=self.cast(cast_results=movie_result["castItems"]))
            for movie_result in movie_results
        ]

    def cast(self, cast_results):
        return [cast_member.name for cast_member in cast_results]