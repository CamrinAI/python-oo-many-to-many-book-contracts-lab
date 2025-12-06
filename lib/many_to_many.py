# * `__init__`: title
# * Class attributes- all
# * Methods:
#   * contracts()- This method should return a list of related contracts
#   * authors()- This method should return a list of related authors using the Contract class as an intermediary

 from turtle import title
from unicodedata import name


class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
