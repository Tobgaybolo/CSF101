# Book class includes attributes like 'title', 'author' and 'availability' of the book.
# Encapsulation: the "Book" class encapsulates attributes('title', 'author', 'is_available')
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    # Shows a string representation of the book
    def __str__(self):
        availability = "Available" if self.is_available else "Borrowed"
        return f"Title: {self.title}, Author: {self.author}, Status: {availability}"

# Library class provides the functionality to 'borrow', 'return' and 'view' books.
class Library:
    def __init__(self):
        self.books = [] # List to store books
        self.borrowed_books = {} # Dictionary to track borrowed books and their borrowers.

    def add_book(self, book):
    # Add new book to the library
        self.books.append(book)

    def view_books(self):
    # Display books and their availability
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books in the Library:")
            for book in self.books:
                print(book)

    def view_available_books(self):
        # Display available books
        available_books = [book for book in self.books if book.is_available]
        if not available_books:
            print("No books available for borrowing.")
        else:
            print("\nAvailable Books:")
            for book in available_books:
                print(book)

    def borrow_book(self, book_title, user_name):
        # Allow user to borrow book if it's available
        for book in self.books:
            if book.title == book_title:
                if book.is_available:
                    # keep the book as borrowed
                    book.is_available = False
                    self.borrowed_books[book_title] = user_name
                    print(f"{user_name} has borrowed '{book_title}'.")
                    return True
                else:
                    # let the user know if the book is borrowed
                    print(f"'{book_title}' is currently borrowed by {self.borrowed_books[book_title]}.")
                    return False
        # let the user know if the book does not exist 
        print(f"The book '{book_title}' is not available in the library.")
        return False

    def return_book(self, book_title, user_name):
        # allow the user to return a book if borrowed
        for book in self.books:
            if book.title == book_title:
                if not book.is_available and self.borrowed_books.get(book_title) == user_name:
                    # make the book available again
                    book.is_available = True
                    del self.borrowed_books[book_title]
                    print(f"{user_name} has returned '{book_title}'.")
                    return True
                else:
                    print(f"'{book_title}' was not borrowed by {user_name} or is already available.")
                    return False
        print(f"The book '{book_title}' does not exist in the library.")
        return False

    def view_borrowed_books(self):
        # show the borrowed books and the user who borrowed it
        if not self.borrowed_books:
            print("No books are currently borrowed.")
        else:
            print("Borrowed Books with User Details:")
            for book_title, user_name in self.borrowed_books.items():
                print(f"'{book_title}' is borrowed by {user_name}.")

# User class represents a library user, with methods to 'borrow' and 'return' books.
class User:
    def __init__(self, name):
        self.name = name
        # Encapsulation: the 'borrowed_books' encapsulates the list of borrowed books.
        self.borrowed_books = []  # List to store book_title, author

    def view_books(self, library):
        # view the books
        library.view_books()

    def borrow_book(self, library, book_title):
        # borrow a book if available
        if library.borrow_book(book_title, self.name):
            # add the book to the borrowed list of user
            for book in library.books:
                if book.title == book_title:
                    self.borrowed_books.append((book_title, book.author))
                    break

    def return_book(self, library, book_title):
        # return book to library
        if library.return_book(book_title, self.name):
            # Remove the book from the user's borrowed_books list
            self.borrowed_books = [(title, author) for title, author in self.borrowed_books if title != book_title]

    def view_borrowed_books(self):
        # Display the borrowed books by uesr
        if not self.borrowed_books:
            print(f"{self.name}'s Borrowed Books:\nYou have not borrowed any books.")
        else:
            print(f"\n{self.name}'s Borrowed Books:")
            for book_title, author in self.borrowed_books:
                print(f"Title: {book_title}, Author: {author}")

# Admin class inherits from the User class and includes additional privileges such as adding new books to the library.
#Inheritance: Admin class inherits from the User class.
class Admin(User):
    def __init__(self, name):
        super().__init__(name)

    # Polymorphism: the 'add_book' is used differently by the 'Admin' class.
    def add_book(self, library, book_title, author):
        # add book
        new_book = Book(book_title, author)
        library.add_book(new_book)
        print(f"Admin {self.name} added '{book_title}' by {author} to the library.")

    def view_borrowed_books(self, library):
        # view borrowed books
        library.view_borrowed_books()

# main function that handles the interactions between 'user', 'admin' and 'library system'.
def main():
    library = Library()
    admin_password = "cap2" # password for admin
    users = {} # dictionary to store the users of the library

    print("Welcome to the CST Library Management System!")

    # main loop that handles the interactions between 'user' and 'admin'.
    while True:
        user_type = input("\nAre you an Admin or a User? (admin/user) OR if you want to exit just enter 'exit': ").lower()

        if user_type == 'admin':
            password = input("Enter Admin password: ")
            if password == admin_password:
                print("...............Accessing Admin...............")
                admin_name = input("\nEnter your name: ")
                if admin_name not in users:
                    users[admin_name] = Admin(admin_name) # create new 'Admin' object

                # admin menu
                while True:
                    print("\nAdmin Menu:")
                    print("1. View all books")
                    print("2. View available books")
                    print("3. Add a book")
                    print("4. View borrowed books with user details")
                    print("5. Exit")

                    admin_choice = input("Choose an option: ")

                    if admin_choice == '1':
                        users[admin_name].view_books(library)

                    elif admin_choice == '2':
                        library.view_available_books()

                    elif admin_choice == '3':
                        book_title = input("Enter the title of the book to add: ")
                        author = input("Enter the author of the book: ")
                        users[admin_name].add_book(library, book_title, author)

                    elif admin_choice == '4':
                        users[admin_name].view_borrowed_books(library)

                    elif admin_choice == '5':
                        print("Exiting Admin Menu.")
                        break

                    else:
                        print("Invalid choice. Please choose a valid option.")

            else:
                print("Incorrect password. Access denied.")

        elif user_type == 'user':
            user_name = input("Enter your name: ")
            if user_name not in users:
                users[user_name] = User(user_name) # create new 'User' object
            
            # user menu
            while True:
                print("\nUser Menu:")
                print("1. View available books")
                print("2. Borrow a book")
                print("3. View your borrowed books")
                print("4. Return a book")
                print("5. Exit")

                user_choice = input("Choose an option: ")

                if user_choice == '1':
                    library.view_available_books()

                elif user_choice == '2':
                    book_title = input("Enter the title of the book to borrow: ")
                    users[user_name].borrow_book(library, book_title)

                elif user_choice == '3':
                    users[user_name].view_borrowed_books()

                elif user_choice == '4':
                    book_title = input("Enter the title of the book to return: ")
                    users[user_name].return_book(library, book_title)

                elif user_choice == '5':
                    print("Exiting User Menu.")
                    break

                else:
                    print("Invalid choice. Please choose a valid option.")

        elif user_type == 'exit':
            print("Thank you for using the CST Library Management System.")
            break

        else:
            print("Invalid input. Please enter 'admin', 'user', or 'exit'.")


if __name__ == "__main__":
    main()
