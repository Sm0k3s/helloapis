from flask import Flask, jsonify, abort, make_response, request

from models import Books, User

app = Flask(__name__)


"""gets all books"""
@app.route('/api/v1/books', methods = ['GET'])
def get_books():
    retrieve_books = Books.get_all_books()
    return jsonify(retrieve_books), 200

"""gets all users"""
@app.route('/api/v1/users')
def get_users():
    get_users = User.get_all_users()
    return jsonify(get_users) , 200

"""gets a single book by id"""
@app.route('/api/v1/books/<int:id>', methods=['GET'])
def get_book(book_id):

    """book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({'book':book[0]})"""

"""gets a single user by id"""
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
