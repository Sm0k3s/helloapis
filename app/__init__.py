from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

books = [
    {   'id':1,
        'title':'Woof',
        'Genre':'Fiction',
        'Synopsis':'A book about dogs'
            },
    {
        'id':2,
        'title':'Mario',
        'Genre':'Gaming',
        'Synopsis':'Mario goes to save princess Peach'
    }
        ]
#gets all books
@app.route('/api/v1/books')
def get_books():
    return jsonify({'books': books})

#gets a single book by id
@app.route('/api/v1/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({'book':book[0]})

#converts error 404 into json
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
