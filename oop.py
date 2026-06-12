# 1. Book class

# Attributes: title, author, year, checked_out (boolean, starts False)
# Methods: check_out(), return_book(), __repr__ (shows title, author, and status)
# Validation: year must be a positive integer
# 2. EBook class (inherits from Book)

# Additional attribute: file_size_mb
# Override __repr__ to include file size
# Override check_out() , ebooks can be checked out by multiple people simultaneously (hint: use a counter instead of a boolean)
# 3. Catalog class

# Methods: add_book(book), search_by_author(author), search_by_title(keyword), get_available(), summary()
# search_by_title should find books where the keyword appears anywhere in the title (case-insensitive)

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        
        # Validation: year must be a positive integer
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer.")
        self.year = year
        
        self.checked_out = False

    def check_out(self):
        if self.checked_out:
            print(f"Sorry, '{self.title}' is already checked out.")
            return False
        self.checked_out = True
        return True

    def return_book(self):
        if not self.checked_out:
            print(f"'{self.title}' was not checked out.")
            return False
        self.checked_out = False
        return True

    def __repr__(self):
        status = "Checked Out" if self.checked_out else "Available"
        return f" '{self.title}' by {self.author} ({self.year}) - [{status}]"
  

class EBook(Book):
    def __init__(self, title, author, year, file_size_mb):
        # Initialize attributes from the parent Book class
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb
        
        # Override check_out tracker to use a counter instead of a boolean
        self.checkout_count = 0 

    def check_out(self):
        # Overridden: Ebooks can be checked out by multiple people simultaneously
        self.checkout_count += 1
        return True

    def return_book(self):
        if self.checkout_count > 0:
            self.checkout_count -= 1
            return True
        print(f"No active checkouts for EBook '{self.title}'.")
        return False

    def __repr__(self):
        # Overridden to include file size and active digital checkout count
        return f"[EBook - {self.file_size_mb}MB] '{self.title}' by {self.author} ({self.year}) - [Active Downloads: {self.checkout_count}]"


class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book or EBook can be added.")

    def search_by_author(self, author):
        # Exact matching using case-insensitive comparison
        return [b for b in self.books if b.author.lower() == author.lower()]

    def search_by_title(self, keyword):
        # Substring matching anywhere in the title (case-insensitive)
        return [b for b in self.books if keyword.lower() in b.title.lower()]

    def get_available(self):
        # EBooks are always available digitally; physical books must not be checked out
        return [b for b in self.books if isinstance(b, EBook) or not b.checked_out]

    def summary(self):
        total = len(self.books)
        available = len(self.get_available())
        
        print(f"\n--- Catalog Summary: {available}/{total} Available ---")
        for book in self.books:
            print(f"  {book}")

catalog = Catalog()
catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))

# Search
results = catalog.search_by_title("python")
print(results)  # Should find "Python Crash Course"

# Check out
catalog.books[0].check_out()
available = catalog.get_available()
print(f"Available: {len(available)} books")

catalog.summary()

             


        