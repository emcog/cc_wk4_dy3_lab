from flask import Flask, render_template, request, redirect
from repositories import author_repository
from repositories import book_repository
from models.author import Author
from models.book import Book
from flask import Blueprint
books_blueprint = Blueprint("books", __name__)



# INDEX
@books_blueprint.route('/books')
def books():
    # get all the books from the DB
    books = book_repository.select_all()
    return render_template('books/index.html', all_books=books)



# NEW
# GET '/books/new'

# CREATE
# POST '/books'

#------> SHOW
# GET '/books/<id>'





# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

## ------->DELETE
# DELETE '/books/<id>'
@books_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_task(id):
    book_repository.delete(id)
    return redirect('/books')