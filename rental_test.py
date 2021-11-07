import unittest
from datetime import datetime
from rental import Rental, PriceCode
from movie import Movie


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.year = datetime.now().year
        self.new_movie = Movie("New", self.year, ["New"])
        self.regular_movie = Movie("Regular", self.year + 1, ["Regular"])
        self.children_movie = Movie("Children", self.year + 1, ["Children"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("CitizenFour", self.year, ["Action"])
        self.assertEqual("CitizenFour", m.get_title())

    def test_rental_price(self):
        """test regular rent price and additional price for exceed the quota"""
        rental = Rental(self.new_movie, 1, PriceCode.NEW_RELEASE)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5, PriceCode.NEW_RELEASE)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.regular_movie, 1, PriceCode.REGULAR)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 6, PriceCode.REGULAR)
        self.assertEqual(rental.get_price(), 8.0)
        rental = Rental(self.children_movie, 2, PriceCode.CHILDREN)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.children_movie, 5, PriceCode.CHILDREN)
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points(self):
        """test frp for movie rented"""
        rental = Rental(self.new_movie, 2, PriceCode.NEW_RELEASE)
        self.assertEqual(rental.get_frp(), 2)
        rental = Rental(self.new_movie, 6, PriceCode.NEW_RELEASE)
        self.assertEqual(rental.get_frp(), 6)
        rental = Rental(self.regular_movie, 1, PriceCode.REGULAR)
        self.assertEqual(rental.get_frp(), 1)
        rental = Rental(self.regular_movie, 7, PriceCode.REGULAR)
        self.assertEqual(rental.get_frp(), 1)
        rental = Rental(self.children_movie, 5, PriceCode.CHILDREN)
        self.assertEqual(rental.get_frp(), 1)
        rental = Rental(self.children_movie, 2, PriceCode.CHILDREN)
        self.assertEqual(rental.get_frp(), 1)

    def test_price_code_factory(self):
        """test price code from factory method"""
        # Price for New Release Movie
        self.assertEqual(PriceCode.NEW_RELEASE, PriceCode.for_movie(self.new_movie))
        # Price for Regular Movie
        self.assertEqual(PriceCode.REGULAR, PriceCode.for_movie(self.regular_movie))
        # Price for Children Movie
        self.assertEqual(PriceCode.CHILDREN, PriceCode.for_movie(self.children_movie))
