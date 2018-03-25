from flask import Flask, jsonify, abort

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

@app.route('/api/v1/books')
def get_books():
    return jsonify({'books': books})

if __name__ == '__main__':
    app.run(debug=True)
