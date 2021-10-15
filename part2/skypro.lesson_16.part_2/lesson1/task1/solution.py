from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Guide(db.Model):
    __tablename__ = 'guide'
    # solution
    id = Column(Integer, primary_key=True)
    name = Column(String)
    main_speciality = Column(String)
    country = Column(String)
    # ------------------------------------


class Excursion(db.Model):
    __tablename__ = 'excursion'
    # solution
    id = Column(Integer, primary_key=True)
    name = Column(String)
    guide_id = Column(Integer, ForeignKey('guide.id'))
    # ------------------------------------
