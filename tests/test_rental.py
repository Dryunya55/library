import unittest
from library.book import Book
from library.reader import Reader
from library.rental import Rental
from datetime import date

class TestRental(unittest.TestCase):

    def setUp(self):
        # Создаем объект Book
        self.book = Book(title="1984", author="George Orwell", year=1949)
        # Создаем объект Reader с именем и email
        self.reader = Reader(name="John Doe", email="johndoe@example.com")
        # Задаем дату аренды
        self.rental_date = date.today()
        # Создаем объект Rental
        self.rental = Rental(self.reader, self.book, self.rental_date)

    def test_rental_initialization(self):
        self.assertEqual(self.rental.book.title, "1984")
        self.assertEqual(self.rental.book.author, "George Orwell")
        self.assertEqual(self.rental.book.year, 1949)
        self.assertEqual(self.rental.reader.name, "John Doe")
        self.assertEqual(self.rental.reader.email, "johndoe@example.com")
        self.assertEqual(self.rental.rental_date, self.rental_date)

    def test_rental_status_not_returned(self):
        self.assertEqual(self.rental.get_rental_status(), "Book not returned")

    def test_return_book(self):
        self.rental.return_book()
        self.assertEqual(self.rental.get_rental_status(), "Book returned")

if __name__ == '__main__':
    unittest.main()
