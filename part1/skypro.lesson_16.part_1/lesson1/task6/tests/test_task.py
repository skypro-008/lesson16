import unittest

import sqlalchemy
from task import db, get_all, get_one


class TestCase(unittest.TestCase):
    def test(self):
        try:
            from task import User
        except ImportError:
            assert False, "Не правильное имя класса User"
        except sqlalchemy.exc.ArgumentError:
            assert False, "Ошибка в синтаксисе модели, не задан атрибут primaryKey или что-то еще"


        db.drop_all()
        db.create_all()

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

        user = get_one(10)
        self.assertEqual(user.email, "mark.loud@mail.com", msg="Не верно работает функция get_one")
        users = get_all()
        print(len(users))
        self.assertEqual(len(users), 10, msg="Не верно работает функция get_all")
        print(users[9].email)
        self.assertEqual(users[9].email, "mark.loud@mail.com", msg="Не верно работает функция get_all")