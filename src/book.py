class Book:
    def init(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def str(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
