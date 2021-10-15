import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Mulan", Movie.new_release)
        self.regular_movie = Movie("CitizenFour", Movie.regular)
        self.children_movie = Movie("Frozen", Movie.children)

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("CitizenFour", Movie.regular)
        self.assertEqual("CitizenFour", m.get_title())
        self.assertEqual(Movie.regular, m.get_price_code())

    def test_rental_price(self):
        """test regular rent price and additional price for exceed the quota"""
        rental = Rental(self.new_movie, 1)  # new_movie
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)  # new_movie (extra cost)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.children_movie, 2)  # children_movie
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.children_movie, 5)  # children_movie (extra cost)
        self.assertEqual(rental.get_price(), 4.5)
        rental = Rental(self.regular_movie, 1)  # regular_movie
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.children_movie, 6)  # regular_movie (extra cost)
        self.assertEqual(rental.get_price(), 6.0)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 2)
        self.assertEqual(rental.get_frp(), 2)
        rental = Rental(self.children_movie, 5)
        self.assertEqual(rental.get_frp(), 1)
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_frp(), 1)
