from datetime import datetime

class Rental:
    def __init__(self, reader, book, rental_date):
        self.reader = reader
        self.book = book
        self.rental_date = rental_date
