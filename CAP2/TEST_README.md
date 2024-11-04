## Library Management System - Test

This repository contain a test for a simple library management system, using pythone's 'unittest' module. The test varifies the functionalities of the 'Library', 'User', and 'Admin' classes, covering main actions ike adding , borrowing and returning books.

## Prerequisites

- python
- The main code file ('CSF101_CAP2_02230288.py') containing the classes 'Library', 'User' and 'Admin'.

## Test Coverage

The test uses 'unittest' to test the following tests:

## 1.Valid Book Borrowing
  - Funtionality: Tests that a user can borrow an available book, which updates the book's availability and registers it in both the user's and the library's record.
  
## 2.Invalid Book Borrowing (Book Already Borrowed)
  - Functionality: Tests that trying to borrow a book that has already been borrowed outputs an appropriate message indicating its unavailability.

## 3.Valid Book Returning
  - Functionality: Test that a user can return a borrowed book, making it available again in the library.

## 4.Invalid Book Returning (Not Borrowed)
  - Functionality: Verifies thst attempting to return a book that hasn't been borrowed prompts an appropriate message.

## 5.Admin Adding Books
  - Functionality: Ensures that an admin can add new books to the library, which increases the total count of available books.

## 6.Boundary and Edge Cases
  - All Books Borrowed: Tests the case where all books in the library are borrowed, ensuring none are left available.
  - Returning Nonexistent Book: Checkes if the system correctly handles an attempt to return a book that does not exist in the library.
  - Returning an Unborrowed Book: Verifies that the system prompts a correct response when trying to return a book the user never borrowed.

## Code Explanation

- unittest: A python unit testing framework used to create test cases.
- unittest.mock.patch: Used to capture printed output (sys.stdout) for verifying the correctness of user-facing messages without altering the main code.

## Running Tests

Each test function corresponds to a particular scenario and varifies its expected behavior:
  - The test will automatically check for expected outputs, correct state changes, and display any assertion errors if test fail.