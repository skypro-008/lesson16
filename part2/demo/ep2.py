import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    passport_number = Column(String(3), unique=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, CheckConstraint("age > 18"))
    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship("Group")


class Group(db.Model):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    users = relationship("User")


db.drop_all()
db.create_all()

# здесь можно дебагом встать и пройти все ограничения чтобы все по очереди показать
# проверяем PK
try:
    jonh = User(id=1, name='jonh', age=30, passport_number="123")
    with db.session.begin():
        db.session.add(jonh)
    jonh1 = User(id=1, name='jonh', age=30, passport_number="123")
    with db.session.begin():
        db.session.add(jonh1)
except Exception as e:
    print(e)

# проверяем unique
try:
    kate = User(id=2, name='kate', age=31, passport_number="123")
    with db.session.begin():
        db.session.add(kate)
except Exception as e:
    print(e)

# проверяем check
try:
    kate = User(id=2, name='kate', age=17, passport_number="890")
    with db.session.begin():
        db.session.add(kate)
except Exception as e:
    print(e)

# проверяем nullable
try:
    kate = User(id=2, name=None, age=30, passport_number="890")
    with db.session.begin():
        db.session.add(kate)
except Exception as e:
    print(e)

# проверяем ForeignKey
# Чтобы заработали FK в SQLite надо настроить SQLAlchemy чтобы она их включила вручную,
# это решение состоит из нескольких строк, но понять их и написать сложнее чем сменить базу,
# поэтому если вам это понадобиться то берите PostgreSQL, мы его будем изучать дальше, через 1,5 месяца.
# try:
#     kate = User(id=2, name="kate", age=30, passport_number="890", group_id=34)
#     with db.session.begin():
#         db.session.add(kate)
# except Exception as e:
#     print(e)

if __name__ == '__main__':
    app.run(debug=True)
