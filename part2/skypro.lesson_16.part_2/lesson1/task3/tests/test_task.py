import unittest

import sqlalchemy


class TestCase(unittest.TestCase):
    def test(self):
        try:
            from task import Singer
        except ImportError:
            self.fail("Не правильное имя класса Singer")
        except sqlalchemy.exc.ArgumentError:
            self.fail("Ошибка в синтаксисе модели, не задан атрибут primaryKey или что-то еще")
        try:
            from task import db
        except ImportError:
            self.fail("Отсутствует переменная db, которая была изначально")

        db.drop_all()
        db.create_all()

        goodSinger = Singer(id=1, name="name1", age=30, group="lessthan30")
        try:
            with db.session.begin():
                db.session.add(goodSinger)
        except Exception as e:
            self.fail(
                "Есть ошибки в модели. Вот такие ХОРОШИЕ данные НЕ вставились: id=1, name='name', age=30, group=\"lessthan30\"")

        duplName = Singer(id=2, name='name1', age=30, group="abcdef")
        was_exception = False
        try:
            with db.session.begin():
                db.session.add(duplName)
        except Exception as e:
            was_exception = True

        if not was_exception:
            self.fail("Есть ошибки в модели. Нет ограничения уникальности колонки name")

        bigAge = Singer(id=3, name='name3', age=40, group="abcdef")
        was_exception = False
        try:
            with db.session.begin():
                db.session.add(bigAge)
        except Exception as e:
            was_exception = True

        if not was_exception:
            self.fail("Есть ошибки в модели. Нет ограничения ограничения возраста (< 35 лет)")

        noneGroup = Singer(id=4, name='name4', age=30, group=None)
        was_exception = False
        try:
            with db.session.begin():
                db.session.add(noneGroup)
        except Exception as e:
            was_exception = True

        if not was_exception:
            self.fail("Есть ошибки в модели. Нет ограничения обязательности (not null) группы")
