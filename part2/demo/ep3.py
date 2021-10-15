import json
from operator import or_, not_

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


db.drop_all()
db.create_all()


def print_result(r):
    print("result:")
    print("id" + " "*(10-2) + "name" + " "*(10-4) + "age" + " "*(10-3) + "group_id")
    for u in r:
        print(str(u.id) + (" "*(10-len(str(u.id))) + str(u.name) + (" "*(10-len(str(u.name))) + str(u.age) + (" "*(10-len(str(u.age))) + str(u.group_id)))))

grp1 = Group(id=1, name="Test Group 1")
grp2 = Group(id=2, name="Test Group 2")

jonh = User(id=1, name='jane', age=20, group=grp1)
kate = User(id=2, name='kate', age=28, group=grp1)
max = User(id=3, name='max', age=32, group=grp2)
maxim = User(id=4, name='maxim', age=38, group=grp2)
mary = User(id=5, name='mary', age=36, group=grp2)
ivan = User(id=6, name=None, age=38, group=grp2)

with db.session.begin():
    db.session.add_all([jonh, kate, max, maxim, mary, ivan])

# тут в дебаггере можно пройтись

# filter

# WHERE
# формируем запрос
q = db.session.query(User).filter(User.name == 'max')
# посмотреть запрос
print(q)
# выполняем запрос
print(q.first().name)

# AND
users = db.session.query(User).filter(User.id <= 5, User.age > 30).all()
print_result(users)

# LIKE
users = db.session.query(User).filter(User.age > 30, User.name.like("ma%")).all()
print_result(users)

# OR
users = db.session.query(User).filter(
    or_(
        User.age < 30,
        User.name.like("ma%")
    )
).all()
print_result(users)

# IS NULL (is не работает)
print_result(db.session.query(User).filter(User.name == None).all())
# IS NOT NULL (not is не работает)
print_result(db.session.query(User).filter(User.name != None).all())
# IN
print_result(db.session.query(User).filter(User.name.in_(['max', 'kate'])).all())
# NOT INT
print_result(db.session.query(User).filter(User.name.notin_(['max', 'kate'])).all())
# BETWEEN
print_result(db.session.query(User).filter(User.age.between(25, 35)).all())

# limit
print_result(db.session.query(User).limit(2).all())
print("-")
print_result(db.session.query(User).filter(User.age > 31).limit(1).all())

# offset
print_result(db.session.query(User).limit(2).offset(2).all())

# order_by
print("all")
print_result(db.session.query(User).filter(User.name.ilike("ma%")).all())
print("")
print("asc")
print_result(db.session.query(User).filter(User.name.ilike("ma%")).order_by(User.age).all())
print("")
print("desc")
from sqlalchemy import desc
print_result(db.session.query(User).filter(User.name.ilike("ma%")).order_by(desc(User.age)).all())

# join (SQL INNER JOIN)
r = db.session.query(User.id, User.name, Group.name.label("grp_name")).join(Group).all()
print("users result:")
print("id" + " "*(10-2) + "name" + " "*(10-4) + "group_name")
for u in r:
    print(str(u.id) + (" "*(10-len(str(u.id))) + str(u.name) + (" "*(10-len(str(u.name))) + u.grp_name)))

# outerjoin (LEFT OUTER JOIN)
gs = db.session.query(
    User.name.label("username"),
    Group.name.label("groupname"),
).outerjoin(Group).all()

print("username" + " "*(10-8) + "groupname")
for u in gs:
    print(str(u.username) + (" "*(10-len(str(u.username))) + str(u.groupname)))

# group_by (сколько пользователей состоит в 1 группе)
from sqlalchemy import func

print(db.session.query(func.count(User.id)).join(Group).filter(Group.id == 1).group_by(Group.id).scalar())
