class Library:
    def __init__(self):
        self.books = []  # Список для зберігання книг

    def add_book(self, book):
        """Метод для додавання книги в бібліотеку."""
        self.books.append(book)

    def rent_book(self, book):
        """Метод для оренди книги."""
        if book in self.books:
            self.books.remove(book)
            return True
        return False

    def return_book(self, book):
        """Метод для повернення книги до бібліотеки."""
        self.books.append(book)
