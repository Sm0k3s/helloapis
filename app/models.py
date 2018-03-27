
library = {}

users = {}


class Books():
    """Books model"""
    def __init__(self):
        self.books = {}

    #gets all books
    def get_all_books():
        return library

    #return a single books
    def get_a_book(self, id):
        return library[id]

    #delete a books
    def delete_book(self, id):
        library.remove('id')
        return library

    #add book
    def add_book(self, title, genre, synopsis, id):
        self.books['title'] = title
        self.books['genre'] = genre
        self.books['synopsis'] = synopsis

        library[id] = self.books

        return library[id]

    #modify a book
    def modify_book(self, title, genre, synopsis):
        self.books['title'] = title
        self.books['genre'] = genre
        self.books['synopsis'] = synopsis


class User():
    """Users model"""
    def __init__(self):
        self.user = {}

    #gets all users
    def get_all_users():
        return users

    #return a single user
    def get_a_user(self, id):
        return users[id]

    #delete a users
    def delete_a_user(self, id):
        users.remove('id')
        return users

    #add a user
    def add_user(self, username, email, id):
        self.user['modify_username'] = title
        self.user['email'] = email
        self.user['id'] = id

        users[id] = self.user

        return users[id]

    #modify a user
    def modify_username(self, username):
        self.user['username'] = username
