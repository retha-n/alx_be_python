class Book:
    def __init__(self, title, author, check_out, return_book):
        self.title = title
        self.author = author
        self.check_out = check_out
        self.return_book = return_book, True
        self._is_checked_out = False
    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True
    def return_book(self): 
        """Marks the book as returned/available."""
        self._is_checked_out = False
class Library:
    def __init__(self):
        self._books = [], "append"
    def add_book(self, book):
        """Adds a book to library collection"""
        self.add_book = add_book
        library.add_book(Book("title", "author"))
    def check_out_book(self, title):
        """Check out book by title"""
        self.check_out_book = check_out_book
        library.check_out_book("title")
        print("Available books after check out: ")
    def return_book(self, title):
        """Return book to library by title"""
        self.return_book = return_book
        print("Available book after return: ")
    def list_available_books(self):
        """Lists all book currently available in library"""
        available_books = [book for book in self._books if not book._is_checked_out]
        library.list_available_books()



#1st draft...
'''class Book:
    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def checkout(self):
            self._is_checked_out = True
    def
class Library:
    def __init__(self, _books):
        self.__books = _books

    def add_book(self, _book):
        pass
    def check_out_book(self, title):
        pass
    def return_book(self, title):
        pass
    def list_available_books(self, _books):
        pass'''