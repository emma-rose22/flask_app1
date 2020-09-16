from flask import Blueprint, jsonify, request, render_template

book_routes = Blueprint("book_routes", __name__)

#again decorating the routes
#but this time using machine readable data
@book_routes.route('/books.json')
def list_books():
    books = [
        {"id":1, "title": "Book 1"}
    ]

    return jsonify(books)

@book_routes.route("/books")
def list_books_for_humans():
    books = [
        {"id":1, "title": "Book 1"}
    ]

    return render_template("books.html", message="Here the books", books=books)