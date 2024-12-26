class Library:
    def init(self):
        self.books = []
        self.readers = []
        self.rentals = []

    def add_book(self, book):
        self.books.append(book)

    def add_reader(self, reader):
        self.readers.append(reader)

    def rent_book(self, reader, book):
        rental = Rental(book, reader)
        self.rentals.append(rental)
        return rental
