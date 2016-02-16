import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

import datetime

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    books = relationship("Book", order_by="Book.id", back_populates="category")

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250))
    publisher = Column(String(250))
    published = Column(Date)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)
    category_id = Column(Integer, ForeignKey('category.id'))

    category = relationship("Category", back_populates="books")

engine = create_engine('postgresql:///catalog')
Base.metadata.create_all(engine)
