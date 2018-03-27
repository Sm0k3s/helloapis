from flask import Flask, jsonify, abort, make_response, request

from models import Books, User, users, library

app = Flask(__name__)

bookworm = Books()

stalker = User()

"""gets all books"""
@app.route('/api/v1/books', methods=['GET'])
def get_books():
    retrieve_books = bookworm.get_all_books()
    return jsonify(retrieve_books), 200

"""gets all users"""
@app.route('/api/v1/users')
def get_users():
    get_users = stalker.get_all_users()
    return jsonify(get_users), 200

"""gets a single book by id"""
@app.route('/api/v1/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    retrieve_book = {retrieve_book for book in library if library[book_id] == book_id}
    return jsonify(retrieve_book), 200


"""gets a single user by id"""
@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    retrieve_user = {retrieve_user for user in users if stalker[user_id] == user_id}
    if len(retrieve_user) == 0:
        abort(404)
    return jsonify(retrieve_user), 200

"""convert error 404 into json"""
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)




if __name__ == '__main__':
    app.run(debug=True)
