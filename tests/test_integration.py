import unittest
from library.book import Book
from library.reader import Reader
from library.rental import Rental
from library.library import Library

class TestLibraryIntegration(unittest.TestCase):
    
    def setUp(self):
        """Цей метод викликається перед кожним тестом"""
        self.library = Library()
        self.book = Book("1984", "George Orwell", 1949)
        self.reader = Reader("Andriitest", "andriitest@example.com")
        self.library.add_book(self.book)

    def test_rent_and_return_book(self):
        """Перевіряємо оренду та повернення книги в бібліотеці"""
        rental = Rental(self.reader, self.book)
        self.library.rent_book(rental)
        self.assertIn(self.book, self.library.rented_books)
        
        self.library.return_book(self.book)
        self.assertNotIn(self.book, self.library.rented_books)
        self.assertIn(self.book, self.library.books)

if __name__ == "__main__":
    unittest.main()
