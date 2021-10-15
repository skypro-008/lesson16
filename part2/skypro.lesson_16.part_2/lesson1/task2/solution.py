from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Author(db.Model):
    __tablename__ = 'author'
    # solution
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    books = relationship("Book")
    # ------------------------------------

class Book(db.Model):
    __tablename__ = 'book'
    # solution
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    copyright = Column(SmallInteger, nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'))
    # ------------------------------------
