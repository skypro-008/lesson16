import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, Text, SmallInteger, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Guide(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    full_name = Column(String)
    tours_count = Column(Integer)
    bio = Column(String)
    is_pro = Column(Boolean)
    company = Column(Integer)

# @app.route("/guides")
# def get_guides():
#     guides = Guide.query.filter(Guide.company > 2).all()
#     r = []
#     for g in guides:
#         if len(r) == 3:
#             break
#         r.append({
#             "surname": g.surname,
#         })
#
#     return r
#
#
# @app.route("/guides/", )
# def get_user(gid: int):
#     g = Guide.query.get(gid)
#     return {
#         "surname": g.surname,
#     }

# solution
@app.route("/guides")
def get_guides():
    guides = Guide.query.all()
    r = []
    for g in guides:
        r.append({
            "id": g.id,
            "surname": g.surname,
            "full_name": g.full_name,
            "tours_count": g.tours_count,
            "bio": g.bio,
            "is_pro": g.is_pro,
            "company": g.company,
        })

    return json.dumps(r)


@app.route("/guides/<int:gid>", )
def get_user(gid: int):
    g = Guide.query.get(gid)
    return json.dumps({
        "id": g.id,
        "surname": g.surname,
        "full_name": g.full_name,
        "tours_count": g.tours_count,
        "bio": g.bio,
        "is_pro": g.is_pro,
        "company": g.company,
    })
# --------------------------------------------------------------------------------
