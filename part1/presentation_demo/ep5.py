import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)


db.create_all()

jonh = User(id=1, name='jonh', age=30)
kate = User(id=2, name='kate', age=31)
max = User(id=3, name='max', age=32)

db.session.add_all([jonh, kate, max])
db.session.commit()


@app.route('/users/first')
def get_first_user():
    u = User.query.first()
    return json.dumps({
        "id": u.id,
        "name": u.name,
        "age": u.age,
    })


@app.route('/users/count')
def get_users_count():
    count = User.query.count()
    return json.dumps(count)


@app.route('/users')
def get_users():
    users = User.query.all()
    res = []
    for u in users:
        res.append({
            "id": u.id,
            "name": u.name,
            "age": u.age,
        })
    return json.dumps(res)


@app.route('/users/<int:sid>')
def get_user(sid: int):
    u = User.query.get(sid)
    return json.dumps({
        "id": u.id,
        "name": u.name,
        "age": u.age,
    })


if __name__ == '__main__':
    app.run(debug=True)
