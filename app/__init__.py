from flask import Flask, jsonify, abort, make_response, request

from data import books, users

app = Flask(__name__)


"""gets all books"""
@app.route('/api/v1/books')
def get_books():
    return jsonify({'books': books})

"""gets all users"""
@app.route('/api/v1/users')
def get_users():
    return jsonify({'users': users})

"""gets a single book by id"""
@app.route('/api/v1/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({'book':book[0]})

"""gets a single book by id"""
@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user':user[0]})

"""convert error 404 into json"""
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)




if __name__ == '__main__':
    app.run(debug=True)
