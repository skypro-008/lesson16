from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, Text, SmallInteger, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


class Guide(db.Model):
    __tablename__ = 'guide'
    # solution
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    full_name = Column(String)
    tours_count = Column(Integer)
    bio = Column(String)
    is_pro = Column(Boolean)
    company = Column(Integer)
    # ------------------------------------


def do_request():
    # solution
    result = db.session.query(Guide).filter(Guide.tours_count > 3).all()
    # ------------------------------------
    return result
