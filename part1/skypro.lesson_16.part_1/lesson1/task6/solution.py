from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, Text, SmallInteger, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    full_name = Column(String)
    city = Column(Integer)
    city_ru = Column(String)


def get_all():
    # solution
    all_users = User.query.all()
    # --------------------------------------------
    return all_users


def get_one(id: int):
    # solution
    one_user = User.query.get(id)
    # --------------------------------------------
    return one_user
