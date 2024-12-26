import unittest
from library.reader import Reader

class TestReader(unittest.TestCase):

    def setUp(self):
        self.reader = Reader("Andriitest", "andriitest@example.com")

    def test_reader_name(self):
        self.assertEqual(self.reader.name, "Andriitest")

    def test_reader_email(self):
        self.assertEqual(self.reader.email, "andriitest@example.com")

if __name__ == '__main__':
    unittest.main()
