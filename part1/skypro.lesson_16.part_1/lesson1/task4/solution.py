from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, Text, SmallInteger, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class City(db.Model):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    timezone = Column(String)
    country = Column(Integer)
    country_ru = Column(String)


db.drop_all()
db.create_all()

# solution
data = [{'name': 'Рим', 'timezone': 'GMT+1', 'country': 3, 'country_ru': 'Италия', 'id': 1},
        {'name': 'Милан', 'timezone': 'GMT+1', 'country': 3, 'country_ru': 'Италия', 'id': 2},
        {'name': 'Венеция', 'timezone': 'GMT+1', 'country': 3, 'country_ru': 'Италия', 'id': 3},
        {'name': 'Стамбул', 'timezone': 'GMT+3', 'country': 4, 'country_ru': 'Турция', 'id': 4},
        {'name': 'Кемер', 'timezone': 'GMT+3', 'country': 4, 'country_ru': 'Турция', 'id': 5},
        {'name': 'Сиде', 'timezone': 'GMT+3', 'country': 4, 'country_ru': 'Турция', 'id': 6},
        {'name': 'Тбилиси', 'timezone': 'GMT+4', 'country': 2, 'country_ru': 'Грузия', 'id': 7},
        {'name': 'Казбеги', 'timezone': 'GMT+4', 'country': 2, 'country_ru': 'Грузия', 'id': 8},
        {'name': 'Хельсинки', 'timezone': 'GMT+2', 'country': 5, 'country_ru': 'Финляндия', 'id': 9},
        {'name': 'Санкт-Петербург', 'timezone': 'GMT+3', 'country': 1, 'country_ru': 'Россия', 'id': 10}]

for d in data:
    city = City(id=d.get("id"),
                name=d.get("name"),
                timezone=d.get("timezone"),
                country=d.get("country"),
                country_ru=d.get("country_ru")
                )

    with db.session.begin():
        db.session.add(city)
# --------------------------------------------
