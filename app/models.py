
from app.data import library, users


class Books():
    """Books model"""
    def __init__(self):
        self.books = {}

    """gets all books from the library dictionary"""
    def get_all_books(self):
        return library

    """return a single books searches a book by its id"""
    def get_a_book(self, book_id):
        return library[0:]['book_id']

    """removes a books from the library"""
    def delete_book(self, book_id):
        library.remove(book_id)
        return library

    """adds a book to library"""
    def add_book(self, title, genre, synopsis, book_id):
        self.title = title
        self.genre = genre
        self.synopsis = synopsis
        self.book_id = book_id
        a_book = {'title': title, 'genre': genre, 'synopsis': synopsis, 'book_id': book_id}
        library.update(a_book)
        return library

    """modify a book"""
    def modify_book(self, title, genre, synopsis):
        self.books['title'] = title
        self.books['genre'] = genre
        self.books['synopsis'] = synopsis


class User():
    """Users model"""
    def __init__(self):
        self.user = {}

    #gets all users
    def get_all_users(self):
        return users

    #return a single user
    def get_a_user(self, user_id):
        return users[user_id]

    #delete a users
    def delete_a_user(self, user_id):
        users.remove(user_id)
        return users

    #add a user
    def add_user(self, username, email, user_id):
        self.user['username'] = username
        self.user['email'] = email
        self.user['id'] = user_id

        users[id] = self.user

        return users[id]

    #modify a user
    def modify_username(self, username):
        self.user['username'] = username
