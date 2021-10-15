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


def print_result(r):
    print("result:")
    print("id" + " " * (10 - 2) + "name" + " " * (10 - 4) + "age" + " " * (10 - 3) + "group_id")
    for u in r:
        print(str(u.id) + (" " * (10 - len(str(u.id))) + str(u.name) + (
                    " " * (10 - len(str(u.name))) + str(u.age) + (" " * (10 - len(str(u.age))) + str(u.group_id)))))


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

# принтим текущую ситуацию
print("BEFORE DELETE №1")
print_result(User.query.all())

# удаление данных №1
print("")
print("DO DELETE №1")
print("")
i = db.session.query(User).get(1)
db.session.delete(i)
db.session.commit()

# принтим текущую ситуацию
print("AFTER DELETE №1")
print_result(User.query.all())

print("")
print("DO DELETE №2")
print("")
# удаление данных №2
User.query.filter(
    User.name.ilike("ma%")
).delete(False)
db.session.commit()

# принтим текущую ситуацию
print("AFTER DELETE №2")
print_result(User.query.all())

if __name__ == '__main__':
    app.run(debug=True)
