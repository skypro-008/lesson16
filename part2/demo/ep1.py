import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship("Group")


class Group(db.Model):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    users = relationship("User")


# дроп тоже дали в презе - ручки на /delete на всякий случйа
db.drop_all()
db.create_all()

# Теперь можно так (тут в дебаггере можно пройтись, а потом перейти к ручкам)

grp100 = Group(id=100, name="Test Group 100")
usr100 = User(id=100, name='jonh doe', age=27, group=grp100)

with db.session.begin():
    db.session.add(usr100)

usr200 = User(id=200, name='michael', age=30)
grp200 = Group(id=200, name="Test Group 200", users=[usr200])

with db.session.begin():
    db.session.add(grp200)


@app.route('/groups')
def get_groups():
    grps = Group.query.all()
    res = []
    for g in grps:
        users = []
        for u in g.users:
            users.append({
                "id": u.id,
                "name": u.name,
                "age": u.age,
            })
        res.append({
            "id": g.id,
            "name": g.name,
            "users": users,
        })

    return json.dumps(res)


@app.route('/groups/create')
def create_groups():
    grp1 = Group(id=1, name="Test Group 1")
    grp2 = Group(id=2, name="Test Group 2")
    with db.session.begin():
        db.session.add(grp1)
        db.session.add(grp2)

    return ''


@app.route('/users/create')
def create_users():
    jonh = User(id=1, name='jonh', age=30, group_id=1)
    kate = User(id=2, name='kate', age=31, group_id=1)
    max = User(id=3, name='max', age=32, group_id=2)

    with db.session.begin():
        db.session.add(jonh)
        db.session.add(kate)
        db.session.add(max)

    return ''


@app.route('/users')
def get_users():
    users = User.query.all()
    res = []
    for u in users:
        res.append({
            "id": u.id,
            "name": u.name,
            "age": u.age,
            "group": {
                "id": u.group.id,
                "name": u.group.name
            }
        })
    return json.dumps(res)


@app.route('/users/delete')
def delete_all_users():
    with db.session.begin():
        User.query.delete()
    return ''


@app.route('/groups/delete')
def delete_all_groups():
    with db.session.begin():
        Group.query.delete()
    return ''


if __name__ == '__main__':
    app.run(debug=True)
