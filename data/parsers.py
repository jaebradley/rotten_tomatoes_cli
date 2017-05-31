from data import TvShowSearchResult, MovieSearchResult, BrowseTvShowResult, BrowseMovieResult


class TvShowSearchResultsParser:
    def __init__(self):
        pass

    def parse(self, tv_show_results):
        return [
            TvShowSearchResult(name=tv_show_result["title"],
                               start_year=tv_show_result["startYear"],
                               end_year=self.year(year=tv_show_result["endYear"]),
                               rotten_tomatoes_score=self.rotten_tomatoes_score(result=tv_show_result))
            for tv_show_result in tv_show_results
        ]

    # Rotten Tomatoes represents the end year for a currently running TV series as 0
    def year(self, year):
        return None if year == 0 else year

    # Sometimes this field is not set
    def rotten_tomatoes_score(self, result):
        return None if "meterScore" not in result else result["meterScore"]


class MovieSearchResultsParser:
    def __init__(self):
        pass

    def parse(self, movie_results):
        return [
            MovieSearchResult(name=movie_result["name"], year=movie_result["year"],
                              rotten_tomatoes_score=self.rotten_tomatoes_score(result=movie_result),
                              cast=self.cast(cast=movie_result["castItems"]))
            for movie_result in movie_results
        ]

    def cast(self, cast):
        return [cast_member["name"] for cast_member in cast]

    # Sometimes this field is not set
    def rotten_tomatoes_score(self, result):
        return None if "meterScore" not in result else result["meterScore"]


class TvShowBrowseResultsParser:
    def __init__(self):
        pass

    def parse(self, tv_show_results):
        return [
            BrowseTvShowResult(title=tv_show_result["title"],
                               rotten_tomatoes_score=self.rotten_tomatoes_score(result=tv_show_result))
            for tv_show_result in tv_show_results
        ]

    # Sometimes this field is not set
    def rotten_tomatoes_score(self, result):
        return None if "tomatoScore" not in result else result["tomatoScore"]


class MovieBrowseResultsParser:
    def __init__(self):
        pass

    def parse(self, movie_results):
        return [
            BrowseMovieResult(title=movie_result["title"],
                              rotten_tomatoes_score=self.rotten_tomatoes_score(result=movie_result),
                              synopsis=movie_result["synopsis"], runtime=self.runtime(result=movie_result),
                              theater_release_date=self.theater_release_date(result=movie_result),
                              dvd_release_date=self.dvd_release_date(result=movie_result),
                              mpaa_rating=movie_result["mpaaRating"], actors=movie_result["actors"])
            for movie_result in movie_results
        ]

    # Sometimes this field is not set
    def rotten_tomatoes_score(self, result):
        return None if "tomatoScore" not in result else result["tomatoScore"]

    # Sometimes this field is not set
    def dvd_release_date(self, result):
        return None if "dvdReleaseDate" not in result else result["dvdReleaseDate"]

    # Sometimes this field is not set
    def theater_release_date(self, result):
        return None if "theaterReleaseDate" not in result else result["theaterReleaseDate"]

    def runtime(self, result):
        return None if "runtime" not in result else result["runtime"]
