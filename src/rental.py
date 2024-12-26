from datetime import date

class Rental:
    def init(self, book, reader):
        self.book = book
        self.reader = reader
        self.rental_date = date.today()
        self.return_date = None

    def return_book(self):
        self.return_date = date.today()
        self.reader.return_book(self.book)
        return f"Book {self.book.title} returned on {self.return_date}"
