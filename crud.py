from models import Book
from database import session
from datetime import date

def add_book(title, author, isbn, count):
    book = Book(title=title, author=author, isbn=isbn, count=count)
    session.add(book)
    session.commit()