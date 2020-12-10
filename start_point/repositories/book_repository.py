from db.run_sql import run_sql

from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository


def save(book):
    sql = 'INSERT INTO books (title, genre, publisher, author, book_id) VALUES (%s, %s, %s, %s) RETURNING *'
    values = [book.title, book.genre, book.publisher, book.author, book.id]
    results = run_sql(sql, values)
    # what is this!?
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []

    sql = 'SELECT * FROM tasks'
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['description'], author, row['pages'], row['id'] )
        books.append(book)
    return books


def select(id):
    book = None
    sql = 'SELECT * FROM books WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['description'], author, row['pages'], row['id'])
    return book


def delete(id):
    sql = 'DELETE FROM tasks WHERE id = %s'
    values = [id]
    run_sql(sql, values)
