"""#from data import books, users
commented this import cause when I run a test
    its keeps telling me no module named 'data' on cmd, am using nosetests

"""
"""books list that stores in dicts"""
books = [
    {   'id':1,
        'title':'Woof',
        'genre':'Fiction',
        'synopsis':'A book about dogs'
            },
    {
        'id':2,
        'title':'Mario',
        'genre':'Gaming',
        'synopsis':'Mario goes to save princess Peach'
    }
        ]
class Books():

    def __init__(self,title,genre,synopsis):
        self.title = title
        self.genre = genre
        self.synopsis = synopsis

    #get all books
    def get_all_books(self):
        return books

    #get a book by id
    def get_a_book(self, book_id):
        return (self.books[book_id])

    #add a book
    def put(self, title, genre, synopsis):
        book = {
            'id': books[-1]['id'] + 1,
            'title': self.title,
            'genre': self.genre,
            'synopsis': self.synopsis
        }
        books.append(book)
