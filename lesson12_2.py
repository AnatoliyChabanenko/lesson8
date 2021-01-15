
class Author:
    def __init__(self, author_name, author_country, author_birthday):
        self.author_name = author_name
        self.author_country = author_country
        self.author_birchday = author_birthday
    def __repr__(self):
            return f'Author {self.author_name} родился в стране {self.author_country} в этот день {self.author_birchday}'
class Book:
    def __init__(self, name, year , author : Author):
        self.name = name
        self.year = year
        self.author = author
    def __repr__(self):
        return f'название { self.name} {self.year } {self.author }'
    def __str__(self):
        return f'{ self.name} {self.year } {self.author }'

class Library:
    books = []
    amount = 0

    def new_book(self, name, year , author: Author):
        self.name = name
        self.year = year
        book= {'name': self.name,
               'year': self.year,
               'author': author
               }
        self.books.append(book)
        Library.amount += 1
    def grop_by_author (self, author: Author):
        return [element for element in self.books if element['author'] == author]

    def group_by_year(self,  year):
        return  [element for element in self.books if element['year'] == year]


    def __repr__(self):
        return f'вот такие книги {self.books}'

    def __str__(self):
        return f'{self.books}'




tom = Author('keisi', 'lisabon', 1995)
gim = Author('gim ', 'kiev', 1995)
a1 = Book('koko',1996,tom)
a13 = Library()
a12 = Library()
a12.new_book('kok', 1996 ,tom)
a13.new_book('kok', 1999 ,gim)
a2= Library()
a2.new_book('kik', 1995 , tom)
print(a12.grop_by_author(gim))
print(a12.group_by_year(1999))


