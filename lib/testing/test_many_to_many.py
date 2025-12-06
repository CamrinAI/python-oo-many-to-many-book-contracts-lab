from many_to_many import Author, Book, Contract
import pytest

def test_book_init():
    """Test Book class initializes with title"""
    book = Book("Title")
    assert book.title == "Title"

def test_author_init():
    """Test Author class initializes with name"""
    author = Author("Name")
    assert author.name == "Name"

def test_contract_init():
    """Test Contract class initializes with author, book, date, royalties"""
    book = Book("Title")
    author = Author("Name")
    date = '01/01/2001'
    royalties = 40000
    contract = Contract(author, book, date, royalties)

    assert contract.author == author
    assert contract.book == book
    assert contract.date == date
    assert contract.royalties == royalties

def test_contract_validates_author():
    """Test Contract class validates author of type Author"""
    book = Book("Title")
    date = '01/01/2001'
    royalties = 40000


