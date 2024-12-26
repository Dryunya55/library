import unittest
from library.book import Book
from library.reader import Reader
from library.rental import Rental
from datetime import datetime

class TestRental(unittest.TestCase):

    def setUp(self):
        self.book = Book("1984", "George Orwell", 1949)
        self.reader = Reader("Andriitest", "andriitest@example.com")
        self.rental = Rental(self.book, self.reader, datetime(2024, 1, 1))

    def test_rental_initialization(self):
        self.assertEqual(self.rental.book.title, "1984")
        self.assertEqual(self.rental.reader.name, "Andriitest")
        self.assertEqual(self.rental.rental_date, datetime(2024, 1, 1))

    def test_rental_status_not_returned(self):
        self.assertEqual(self.rental.get_rental_status(), "Book not returned")

    def test_return_book(self):
        self.rental.return_book()
        self.assertTrue(self.rental.return_date)
        self.assertNotEqual(self.rental.return_date, datetime(2024, 1, 1))  # Перевірка, що повернення не сталося в день оренди
        self.assertIn("Returned", self.rental.get_rental_status())

if __name__ == '__main__':
    unittest.main()

