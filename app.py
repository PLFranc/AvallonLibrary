from flask import Flask, jsonify, request

import models

app = Flask(__name__)

books = [
    {
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'available': True,
    },
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city '
                       'Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]



@app.route('/add_book', methods=['POST'])
def add_book():
    book =request.get_json()
    book['available'] = True
    models.add_book(book)
    book = models.get_specific_book_by_title(request.get_json()['title'])
    print(book)
    models.add_book_in_area(book_id=book[0])
    return jsonify({'item': 'Book added'}), 201


@app.route('/getbooks', methods=['GET'])
def get_books():
    results = models.get_books()
    return jsonify(results)


@app.route('/add_user', methods=['POST'])
def add_user():
    user = request.get_json()
    user['admin'] = False
    print(user)
    models.add_user(user)
    return jsonify({'item': 'user added'}), 201


# @app.route('/connection', methods=['POST'])
# def connection():
#     email = request.get_json()['email']
#     password = request.get_json()['password']
#     currentUser = models.connection(email, password)
#     if currentUser == 'error':
#         currentUser = None
#         return jsonify({'message': 'erreur de connection'}), 201
#     else:
#         return jsonify({'message': 'user connected'}), 201


@app.route('/make_reservation', methods=['PUT'])
def make_reservation():
    models.make_reservation(request.get_json()['user_id'], request.get_json()['book_id'])
    models.remove_book_of_storage(request.get_json()['book_id'])
    return jsonify({'message': 'book reserved'}), 201


@app.route('/brought_book', methods=['PUT'])
def brought_book():
    models.brought_book(request.get_json()['book_id'])
    models.add_book_in_area(book_id=request.get_json()['book_id'])
    return jsonify({'message': 'book returned'})


@app.route('/reservations', methods=['GET'])
def get_reservation():
    reservations = models.get_reservation()
    return jsonify(reservations)

@app.route('/store_book', methods=['PUT'])
def modify_book_area():
    models.modify_book_area(request.get_json()['area'], request.get_json()['rack'], request.get_json()['book_id'])
    return jsonify({'message': 'book stored'})

@app.route('/get_available_book', methods=['GET'])
def get_available_book():
    results = models.get_available_book()
    return jsonify(results)

@app.route('/get_book_by_title', methods=['GET'])
def get_book_by_title():
    result = models.get_specific_book_by_title(request.get_json()['title'])
    return jsonify(result)

@app.route('/get_book_by_author', methods=['GET'])
def get_book_by_author():
    result = models.get_specific_book_by_author(request.get_json()['author'])
    return jsonify(result)


@app.route('/get_book_area', methods=['GET'])
def get_book_area():
    result = models.get_book_area(request.get_json()['book_id'])
    return jsonify(result)

if __name__ == '__main__':
    app.run()
