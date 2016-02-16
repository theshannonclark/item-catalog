from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#from database_setup import Base, Category, Book

#engine = create_engine('postgresql:///catalog')
#Base.metadata.bind = engine

#DBSession = sessionmaker(bind = engine)
#session = DBSession()

categories = [
    {'name': 'Arts & Photography'},
    {'name': 'Fantasy'},
    {'name': 'Science Fiction'}
]

books = [
    {'name': 'The Name of the Wind'},
    {'name': 'The Lies of Locke...'},
    {'name': 'Perdido Street Station'},
    {'name': 'Gardens of the Moon'},
    {'name': 'The Way of Kings'}
]

@app.route('/')
def home():
    return render_template("index.html", categories=categories, books=books)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
