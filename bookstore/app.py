from flask import Flask, render_template, request

app = Flask(__name__)

# List of books (example data)
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "image": "book1.jpeg", "likes": 0},
    {"id": 2, "title": "Book 2", "author": "Author 2", "image": "book2.jpeg", "likes": 0},
    {"id": 3, "title": "Book 3", "author": "Author 3", "image": "book2.jpeg", "likes": 0},
    # Add more books as needed
]

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html', books=books)

# Route for displaying book details
@app.route('/book/<int:book_id>')
def book_details(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return render_template('book_details.html', book=book)
    else:
        return "Book not found", 404

# Route for handling likes
@app.route('/like', methods=['POST'])
def like():
    book_id = int(request.form['book_id'])
    for book in books:
        if book['id'] == book_id:
            book['likes'] += 1
            break
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
