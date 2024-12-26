class Reader:
    def init(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available_copies > 0:
            self.borrowed_books.append(book)
            book.available_copies -= 1
            return f"{self.name} borrowed {book.title}"
        else:
            return f"{book.title} is not available for borrowing."

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available_copies += 1
            return f"{self.name} returned {book.title}"
        else:
            return f"{self.name} did not borrow {book.title}"
