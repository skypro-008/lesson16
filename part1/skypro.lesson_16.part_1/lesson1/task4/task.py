from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, Text, SmallInteger, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class City(db.Model):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    timezone = Column(String)
    country = Column(Integer)
    country_ru = Column(String)


db.drop_all()
db.create_all()