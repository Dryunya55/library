import unittest
from library.book import Book
from library.reader import Reader
from library.rental import Rental
from datetime import date

class TestLibrary(unittest.TestCase):

    def setUp(self):
        # Создаем объект Book
        self.book = Book(title="1984", author="George Orwell", year=1949)
        # Создаем объект Reader с именем и email
        self.reader = Reader(name="John Doe", email="johndoe@example.com")
        # Создаем объект Rental
        self.rental = Rental(self.reader, self.book, date.today())

    def test_rent_book(self):
        """Тестируем аренду книги"""
        self.assertEqual(self.rental.book.title, "1984")
        self.assertEqual(self.rental.reader.name, "John Doe")

    def test_return_book(self):
        """Тестируем возврат книги"""
        self.rental.return_book()
        self.assertEqual(self.rental.get_rental_status(), "Book returned")

if __name__ == '__main__':
    unittest.main()
