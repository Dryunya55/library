import unittest
from library.book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book("1984", "George Orwell", 1949)

    def test_book_title(self):
        self.assertEqual(self.book.title, "1984")

    def test_book_author(self):
        self.assertEqual(self.book.author, "George Orwell")

    def test_book_year(self):
        self.assertEqual(self.book.year, 1949)

if __name__ == '__main__':
    unittest.main()
