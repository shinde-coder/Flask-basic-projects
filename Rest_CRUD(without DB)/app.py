from flask import Flask, request

app = Flask(__name__)

# Sample data (can be replaced with a database)
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'},
    {'id': 3, 'title': 'Book 3', 'author': 'Author 3'}
]

# Get all records
@app.route("/", methods=['GET'])
def get_books():
    return {'books': books}
@app.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return book
    return {'error': 'Book not found'}
@app.route('/', methods=['POST'])
def create_book():
    new_book = {'id': len(books) + 1, 'title': request.json['title'], 'author': request.json['author']}
    books.append(new_book)
    return new_book
@app.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id']==book_id:
            book['title']=request.json['title']
            book['author']=request.json['author']
            return book 
    return {'error':'Book not found'}

@app.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book[id] == book_id :
            books.remove(book)
            return {"data":"Book Deleted"}
    return {'error': 'Book not found'}

# @app.route('/<int:book_id>', methods=['DELETE'])
# def delete_book(book_id):
#     for book in books:
#         if book['id']==book_id:
#             books.remove(book)
#             return {"data":"Book Deleted Successfully"}

#     return {'error':'Book not found'}




if __name__ == "__main__":
    app.run(debug=True)
