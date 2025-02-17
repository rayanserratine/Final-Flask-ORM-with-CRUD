from flask import request, jsonify
from models import db, User, Book, Author, Borrow
from datetime import datetime

# User CRUD
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created!"}), 201

def get_all_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name, "email": user.email} for user in users])

def get_user_by_id(id):
    user = User.query.get_or_404(id)
    return jsonify({"id": user.id, "name": user.name, "email": user.email})

def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify({"message": "User updated!"})

def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted!"})

# Book CRUD
def create_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author_id=data['author_id'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book created!"}), 201

def get_all_books():
    books = Book.query.all()
    return jsonify([{"id": book.id, "title": book.title, "author_id": book.author_id} for book in books])

def get_books_by_author(author_id):
    books = Book.query.filter_by(author_id=author_id).all()
    return jsonify([{"id": book.id, "title": book.title} for book in books])

def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted!"})

# Author CRUD
def create_author():
    data = request.get_json()
    new_author = Author(name=data['name'])
    db.session.add(new_author)
    db.session.commit()
    return jsonify({"message": "Author created!"}), 201

def get_all_authors():
    authors = Author.query.all()
    return jsonify([{"id": author.id, "name": author.name} for author in authors])

def get_author_books(id):
    author = Author.query.get_or_404(id)
    books = author.books
    return jsonify([{"id": book.id, "title": book.title} for book in books])

# Borrow CRUD
def borrow_book():
    data = request.get_json()
    new_borrow = Borrow(user_id=data['user_id'], book_id=data['book_id'])
    db.session.add(new_borrow)
    db.session.commit()
    return jsonify({"message": "Book borrowed!"}), 201

def get_borrowed_books_by_user(user_id):
    borrows = Borrow.query.filter_by(user_id=user_id).all()
    return jsonify([{"book_id": borrow.book_id, "borrow_date": borrow.borrow_date} for borrow in borrows])

def get_users_by_book(book_id):
    borrows = Borrow.query.filter_by(book_id=book_id).all()
    return jsonify([{"user_id": borrow.user_id, "borrow_date": borrow.borrow_date} for borrow in borrows])