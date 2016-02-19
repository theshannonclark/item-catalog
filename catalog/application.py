from flask import Flask, render_template, request, redirect, url_for, abort
app = Flask(__name__)

from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Book

engine = create_engine('postgresql:///catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
def home():
	categories = session.query(Category).order_by(Category.name).all()
	recent_books = session.query(Book).order_by(desc(Book.created_at))[0:5]

	return render_template("index.html", categories=categories, recent=recent_books)

@app.route('/catalog/<category>')
def category(category):
	categories = session.query(Category).order_by(Category.name).all()
	selected = [c for c in categories if c.slug == category]
	if len(selected) == 1:
		selected_name = selected[0].name
		books = selected[0].books
	else:
		abort(404)

	return render_template("category.html", category=selected_name, categories=categories, books=books)

@app.route('/catalog/book/<int:book_id>')
def item(book_id):
	book = None
	book_list = session.query(Book).filter_by(id = book_id).all()
	if len(book_list) == 1:
		book = book_list[0]
	else:
		abort(404)

	return render_template("item.html", book=book)

@app.route('/catalog/')
def nope():
	return redirect(url_for('home'))

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
