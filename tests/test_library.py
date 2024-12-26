import unittest
from src.library import Library
from src.book import Book
from src.reader import Reader
from src.rental import Rental

class TestLibrary(unittest.TestCase):
    
    def setUp(self):
        """Цей метод викликається перед кожним тестом"""
        self.library = Library()
        self.book = Book("1984", "George Orwell", 1949)
        self.reader = Reader("Andriitest", "andriitest@example.com")
        self.library.add_book(self.book)

    def test_add_book(self):
        """Тестуємо додавання книги до бібліотеки"""
        self.assertIn(self.book, self.library.books)

    def test_rent_book(self):
        """Тестуємо оренду книги"""
        rental = Rental(self.reader, self.book)
        self.library.rent_book(rental)
        self.assertIn(self.book, self.library.rented_books)
    
    def test_return_book(self):
        """Тестуємо повернення книги до бібліотеки"""
        rental = Rental(self.reader, self.book)
        self.library.rent_book(rental)
        self.library.return_book(self.book)
        self.assertNotIn(self.book, self.library.rented_books)
        self.assertIn(self.book, self.library.books)

if __name__ == "__main__":
    unittest.main()

