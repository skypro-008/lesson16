from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, Text, SmallInteger, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    full_name = Column(String)
    city = Column(Integer)
    city_ru = Column(String)


db.drop_all()
db.create_all()

# solution
data = [{'email': 'novlu@mail.com', 'password': 'mkdXjIjYM', 'full_name': 'Людмила Новикова', 'city': 10,
         'city_ru': 'Санкт-Петербург', 'id': 1},
        {'email': 'tripper678@yahhaa.com', 'password': 'eGGPtRKS5', 'full_name': 'Андрей Васечкин', 'city': 11,
         'city_ru': 'Москва', 'id': 2},
        {'email': 'georgiberidze@mail.com', 'password': 'NWRV0Z9ZC', 'full_name': 'Георги Беридзе', 'city': 7,
         'city_ru': 'Тбилиси', 'id': 3},
        {'email': 'oksi.laslas89@mail.com', 'password': 'TenhtQOjv', 'full_name': 'Оксана Ласкина', 'city': 12,
         'city_ru': 'Казань', 'id': 4},
        {'email': 'vanyahot888@inmail.com', 'password': '5YGRPtYlw', 'full_name': 'Иван Горячий', 'city': 13,
         'city_ru': 'Сочи', 'id': 5},
        {'email': 'yanaturkiy@mail.com', 'password': 'rN3HI4elT', 'full_name': 'Яна Ивлева', 'city': 4,
         'city_ru': 'Стамбул', 'id': 6},
        {'email': 'irafromrome@yahhaa.com', 'password': 'mWmSmkNsD', 'full_name': 'Ирина Самидзе', 'city': 1,
         'city_ru': 'Рим', 'id': 7},
        {'email': 'pskovstalker@mail.com', 'password': 'M572gH5lG', 'full_name': 'Владислав Ванькин', 'city': 14,
         'city_ru': 'Псков', 'id': 8},
        {'email': 'dinadina13@mail.com', 'password': 'v2dSbgPYb', 'full_name': 'Дина Левинова', 'city': 9,
         'city_ru': 'Хельсинки', 'id': 9},
        {'email': 'mark.loud@mail.com', 'password': 'pz4ZIYu1l', 'full_name': 'Марк Звонкий', 'city': 15,
         'city_ru': 'Нижний Новгород', 'id': 10}]

for d in data:
    user = User(
        id=d.get("id"),
        email=d.get("email"),
        password=d.get("password"),
        full_name=d.get("full_name"),
        city=d.get("user"),
        city_ru=d.get("city_ru"),
    )

    with db.session.begin():
        db.session.add(user)
# --------------------------------------------
