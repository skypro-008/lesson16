from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, Text, SmallInteger, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Guide(db.Model):
    __tablename__ = 'guide'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    full_name = Column(String)
    tours_count = Column(Integer)
    bio = Column(String)
    is_pro = Column(Boolean)
    company = Column(Integer)


def update_tours_count():
    # solution
    g = Guide.query.get(1)
    g.tours_count = 6
    db.session.add(g)
    db.session.commit()
    # ------------------------------------
