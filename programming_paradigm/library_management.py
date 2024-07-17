# library_management.py

class Book:
    """A class representing a book with a title and an author."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        self._is_checked_out = True
    
    def return_book(self):
        self._is_checked_out = False
    
    def is_available(self):
        return not self._is_checked_out


class Library:
    """A class representing a library that can manage multiple books."""
    
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"Book '{title}' checked out."
        return f"Book '{title}' not available or does not exist."
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"Book '{title}' returned."
        return f"Book '{title}' was not checked out or does not exist."
    
    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")
        if not available_books:
            print("No available books.")

