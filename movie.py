import csv
from typing import List


class Movie:
    """
    A movie available for rent.
    """

    # The types of movies (price_code).
    def __init__(self, title, year, genre):
        # Initialize a new movie.
        self._title: str = title
        self._genre: List[str] = genre
        self._year: int = year

    def get_title(self):
        # function to get the value of _title
        return self._title

    def get_year(self):
        # function to get the value of _year
        return self._year

    def is_genre(self, genre: str) -> bool:
        return genre in self._genre

    def get_price_code(self):
        # function to get the value of price_code
        return self.price_code

    def __str__(self) -> str:
        return self._title


class MovieCatalog:
    catalog = "movies.csv"

    def __init__(self) -> None:
        self.data = {}
        with open(self.catalog) as f:
            reader = csv.DictReader(f)
            for line in reader:
                self.data[line["title"]] = {
                    "id": line["#id"],
                    "genre": [i for i in line["genres"].split("|")],  # Some movie has more than one genre.
                    "year": int(line["year"]),
                }

    def get_movie(self, title: str) -> Movie:
        # function to get the Movie
        movie_data = self.data[title]
        return Movie(title, movie_data["year"], movie_data["genre"])
