# import pytest
#
#
# def add(a, b):
#     return a + b
#
#
# @pytest.mark.skip(reason="not yet")
# def test_add():
#     assert add(1, 2) == 3
#
#
# def test_fail():
#     assert False
import pytest
from book import Book
from library import Library

@pytest.fixture
def library():
    """יצירת מופע חדש של הספרייה לפני כל בדיקה"""
    lib = Library()
    lib.add_user("Alice")  # הוספת משתמש לבדיקה
    return lib

def test_add_book_success(library):
    """בדיקה שהספר נוסף בהצלחה לרשימת הספרים"""
    book = Book("Harry Potter", "J.K. Rowling")
    library.add_book(book)
    print("after add book")
    assert book in library.books

def test_add_book_empty_title_or_author(library):
    """בדיקה שהמערכת מונעת הוספת ספר עם כותרת או מחבר ריקים"""
    b1 = Book("", "J.K. Rowling")  # כותרת ריקה
    library.add_book(b1)
    assert b1 in library.books
    b2 = Book("Harry Potter", "")  # מחבר ריק
    library.add_book(b2)
    assert b2 in library.books


def test_add_book_special_characters_and_numbers(library):
    """בדיקה שהמערכת מאפשרת הוספת ספרים עם תווים מיוחדים ומספרים"""
    book = Book("C++ Programming 101", "Dr. John@Doe")
    library.add_book(book)
    assert book in library.books

def test_add_user_success(library):
    library.add_user("Alice")
    assert "Alice" in library.users

def test_check_out_book_successfully_loaned_to_a_registered_user(library):
    username = "Rivky Hailbron"
    library.add_user(username)
    book = Book("Harry Potter", "J.K. Rowling")
    library.add_book(book)
    library.check_out_book(username,book)
    print(f"books {library.books}")
    print(f"users {library.users}")
    print(f"check_out_books {library.checked_out_books}")
    assert book.is_checked_out is True
    assert library.checked_out_books[username] == book

def test_return_book_was_not_borrowed_at_all(library):
    """✅ בדיקה שהמערכת מונעת החזרת ספר שלא הושאל כלל.
 """
    book = Book("Harry Potter", "J.K. Rowling")
    assert library.return_book(library.users[0] , book)