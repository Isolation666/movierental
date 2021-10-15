# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer


def make_movies():
    movies = [
        Movie("The Irishman", Movie.new_release),
        Movie("CitizenFour", Movie.regular),
        Movie("Frozen", Movie.children),
        Movie("El Camino", Movie.new_release),
        Movie("Particle Fever", Movie.regular)
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
