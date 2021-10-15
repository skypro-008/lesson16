import unittest

import sqlalchemy


class TestCase(unittest.TestCase):
    def test(self):
        try:
            from task import Guide, Excursion
        except ImportError:
            self.fail("Не правильное имя класса Guide, Excursion")
        except sqlalchemy.exc.ArgumentError:
            self.fail("Ошибка в синтаксисе модели, не задан атрибут primaryKey или что-то еще")
        try:
            from task import db
        except ImportError:
            self.fail("Отсутствует переменная db, которая была изначально")

        db.drop_all()
        db.create_all()

        guide = Guide(id=1, name='name', main_speciality="spec", country="Russia")
        exc = Excursion(id=1, name='name', guide_id=1)

        with db.session.begin():
            db.session.add(guide)
        with db.session.begin():
            db.session.add(exc)
