class Rental:
    def __init__(self, reader, book, rental_date):
        self.reader = reader
        self.book = book
        self.rental_date = rental_date
        self.returned = False  # Атрибут для отслеживания, возвращена ли книга

    def get_rental_status(self):
        """Возвращает статус аренды"""
        if not self.returned:
            return "Book not returned"
        return "Book returned"

    def return_book(self):
        """Метод для возврата книги"""
        self.returned = True
