import unittest
# patch is a form of MOCKING that enables us to indirectly verify the output without altering he original code.
from unittest.mock import patch
from io import StringIO

# Importing the classes 'Library', 'User', and 'Admin' from our main code
from CSF101__CAP2_02230288 import Library, User, Admin

class TestLibraryManagementSystem(unittest.TestCase):
    
    def setUp(self):
        # Setting up a test 'Library', 'Admin' and 'User' for testing
        self.library = Library()
        self.admin = Admin("Admin User")
        self.user = User("Test User")

        # Admin adds the books to the library for testing
        self.admin.add_book(self.library, "Book A", "Author A")
        self.admin.add_book(self.library, "Book B", "Author B")

    def test_borrow_book(self):
        # Test if a user can borrow an available book
        self.user.borrow_book(self.library, "Book A")
        self.assertIn("Book A", self.library.borrowed_books)
        self.assertFalse(self.library.books[0].is_available)
        self.assertIn(("Book A", "Author A"), self.user.borrowed_books)

    def test_borrow_book_already_borrowed(self):
        # Test borrowing a book that is already borrowed
        self.user.borrow_book(self.library, "Book A")
        another_user = User("Another User")

        with patch('sys.stdout', new=StringIO()) as fake_output: # "patch('sys.stdout', new=StringIO())" replaces "sys.stdout" with a "StringIO" object "fake_output", which collects the printed texts. 
            another_user.borrow_book(self.library, "Book A")
            self.assertIn("currently borrowed by Test User", fake_output.getvalue()) # "fake_output.getvalue()" retrieves all the printed texts, which allows us to if the printed texts were indeed printed.

    def test_return_book(self):
        # Test if a user can return a borrowed book
        self.user.borrow_book(self.library, "Book A")
        self.user.return_book(self.library, "Book A")

        self.assertNotIn("Book A", self.library.borrowed_books)
        self.assertTrue(self.library.books[0].is_available)
        self.assertNotIn(("Book A", "Author A"), self.user.borrowed_books)

    def test_return_book_not_borrowed(self):
        # Test returning a book that was not borrowed
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.user.return_book(self.library, "Book A")
            self.assertIn("was not borrowed by Test User or is already available", fake_output.getvalue())

    def test_admin_add_book(self):
        # Ensure that the admin can add a new book to athe library
        self.admin.add_book(self.library, "Book C", "Author C")
        self.assertEqual(len(self.library.books), 3)
        self.assertEqual(self.library.books[-1].title, "Book C")

    def test_borrow_all_books(self):
        # Test borrowing all books and ensure none are left available
        self.user.borrow_book(self.library, "Book A")
        self.user.borrow_book(self.library, "Book B")

        available_books = [book for book in self.library.books if book.is_available]
        self.assertEqual(len(available_books), 0)

        another_user = User("Another User")
        self.assertFalse(another_user.borrow_book(self.library, "Book A"))

    def test_return_nonexistent_book(self):
        # Test returning a book that does not exist in the library
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.user.return_book(self.library, "Nonexistent Book")
            self.assertIn("does not exist in the library", fake_output.getvalue())

    def test_return_unborrowed_book(self):
        # Test returning a book that the user never borrowed
        self.admin.add_book(self.library, "Book C", "Author C")

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.user.return_book(self.library, "Book C")
            self.assertIn("was not borrowed by Test User or is already available", fake_output.getvalue())

# Run tests
if __name__ == "__main__":
    unittest.main()
