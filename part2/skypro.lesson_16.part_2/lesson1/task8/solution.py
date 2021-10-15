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
    __tablename__ = 'guide'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    full_name = Column(String)
    tours_count = Column(Integer)
    bio = Column(String)
    is_pro = Column(Boolean)
    company = Column(Integer)


# solution
# 1, 3
@app.route("/guides")
def find_by_tc():
    tours_count = request.args.get("tours_count")
    guides = Guide.query.all()
    r = []
    if tours_count:
        for g in guides:
            if g.tours_count == int(tours_count):
                r.append({
                    "id": g.id,
                    "surname": g.surname,
                    "full_name": g.full_name,
                    "tours_count": g.tours_count,
                    "bio": g.bio,
                    "is_pro": g.is_pro,
                    "company": g.company,
                })
    else:
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


# 2, 4, 5
@app.route("/guides/<int:gid>", methods=['GET', 'POST', 'PUT'])
def find_by_id(gid: int):
    if request.method == "GET":
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
    elif request.method == "POST":
        Guide.query.filter(Guide.id == gid).delete(False)
        db.session.commit()
        return "", 204
    elif request.method == "PUT":
        g = Guide.query.get(gid)
        data = json.loads(request.data)
        if "surname" in data:
            g.surname = data.get("surname")
        if "full_name" in data:
            g.full_name = data.get("full_name")
        if "tours_count" in data:
            g.tours_count = data.get("tours_count")
        db.session.commit()
        return "", 204
# --------------------------------------------------------------------------------
