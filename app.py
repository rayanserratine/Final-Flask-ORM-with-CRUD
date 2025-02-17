from flask import Flask
from models import db
from routes import (
    create_user, get_all_users, get_user_by_id, update_user, delete_user,
    create_book, get_all_books, get_books_by_author, delete_book,
    create_author, get_all_authors, get_author_books,
    borrow_book, get_borrowed_books_by_user, get_users_by_book
)
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# User Routes
app.add_url_rule('/users', 'create_user', create_user, methods=['POST'])
app.add_url_rule('/users', 'get_all_users', get_all_users, methods=['GET'])
app.add_url_rule('/users/<int:id>', 'get_user_by_id', get_user_by_id, methods=['GET'])
app.add_url_rule('/users/<int:id>', 'update_user', update_user, methods=['PUT'])
app.add_url_rule('/users/<int:id>', 'delete_user', delete_user, methods=['DELETE'])

# Book Routes
app.add_url_rule('/books', 'create_book', create_book, methods=['POST'])
app.add_url_rule('/books', 'get_all_books', get_all_books, methods=['GET'])
app.add_url_rule('/books/author/<int:author_id>', 'get_books_by_author', get_books_by_author, methods=['GET'])
app.add_url_rule('/books/<int:id>', 'delete_book', delete_book, methods=['DELETE'])

# Author Routes
app.add_url_rule('/authors', 'create_author', create_author, methods=['POST'])
app.add_url_rule('/authors', 'get_all_authors', get_all_authors, methods=['GET'])
app.add_url_rule('/authors/<int:id>/books', 'get_author_books', get_author_books, methods=['GET'])

# Borrow Routes
app.add_url_rule('/borrow', 'borrow_book', borrow_book, methods=['POST'])
app.add_url_rule('/user/<int:user_id>/borrowed_books', 'get_borrowed_books_by_user', get_borrowed_books_by_user, methods=['GET'])
app.add_url_rule('/book/<int:book_id>/users', 'get_users_by_book', get_users_by_book, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)