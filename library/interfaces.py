from abc import ABC, abstractmethod

class IBook(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

class IReader(ABC):
    @abstractmethod
    def borrow_book(self, book):
        pass

class IRental(ABC):
    @abstractmethod
    def return_book(self):
        pass
