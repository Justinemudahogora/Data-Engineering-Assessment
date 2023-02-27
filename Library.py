class LibraryBook:
    def __init__(self, title, author, publication_year, isbn):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.checked_out = False

    def check_out(self):
        if self.checked_out:
            print(f"{self.title} is already checked out.")
        else:
            self.checked_out = True
            print(f"{self.title} has been checked out.")

    def check_in(self):
        if not self.checked_out:
            print(f"{self.title} is not checked out.")
        else:
            self.checked_out = False
            print(f"{self.title} has been checked in.")



class Library:
    def __init__(self):
        self.books = []
        self.total_books = 0
        self.available_books = 0

    def add_book(self, title, author, publication_year, isbn):
        book = LibraryBook(title, author, publication_year, isbn)
        self.books.append(book)
        self.total_books += 1
        self.available_books += 1

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            self.total_books -= 1
            if not book.checked_out:
                self.available_books -= 1

    def search_books(self, term):
        results = []
        for book in self.books:
            if term.lower() in book.title.lower():
                results.append(book)
        if len(results) == 0:
            print(f"No books found matching '{term}'.")
        else:
            print(f"Found {len(results)} book(s) matching '{term}':")
            for book in results:
                print(f"{book.title} by {book.author}")

    def list_books(self):
        print(f"Total books: {self.total_books}")
        print(f"Available books: {self.available_books}")
        print("All books in the library:")
        for book in self.books:
            status = "Available" if not book.checked_out else "Checked out"
            print(f"{book.title} by {book.author} ({book.publication_year}), ISBN: {book.isbn} - {status}")


# Create a new library object.
library = Library()

# Add three new books to the library.
library.add_book("Python for Backend", "Justine MUDAHOGORA", 2023, "12345")
library.add_book("Full Course Python", "Major RUGARUZA", 2022, "123456")
library.add_book("Python for beginners", "Simon MUTUNZI", 2021, "1234567")

# Search for books with the search term "Python" and print the results.
library.search_books("Python")

# Check out one of the books.
library.books[0].check_out()

# List all of the books in the library.
library.list_books()

# Check in the book that was checked out.
library.books[0].check_in()

# List all of the books in the library again to verify that the book was checked in successfully.
library.list_books()
