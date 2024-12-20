from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)

@api_bp.route("/api/books", methods=["GET"])
def get_books():
    books = [
        {"id": 1, "title": "Book 1", "author": "Author 1"},
        {"id": 2, "title": "Book 2", "author": "Author 2"},
        {"id": 3, "title": "Book 3", "author": "Author 3"},
    ]
    return jsonify(books)
