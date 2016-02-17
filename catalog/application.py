from flask import Flask, render_template, request, redirect, url_for
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

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
