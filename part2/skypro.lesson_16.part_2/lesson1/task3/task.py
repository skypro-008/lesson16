from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, SmallInteger, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# solution
class Singer(db.Model):
    __tablename__ = 'singer'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    age = Column(Integer, CheckConstraint("age < 35"))
    group = Column(String, nullable=False)
# ------------------------------------