from data import books, users

class Books(self):
    def __init__(self):
        self.books = {}

    #get all books
    def get_all_books(self):
        return books

    #get a book by id
    def get_a_book(self, book_id):
        return (self.books[book_id])

    #add a books
    def put(self, title, genre, book_id):
        book = {

        }
