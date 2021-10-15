import unittest

import sqlalchemy
from task import db


class TestCase(unittest.TestCase):
    def test(self):
        try:
            from task import City
        except ImportError:
            assert False, "Не правильное имя класса City"
        except sqlalchemy.exc.ArgumentError:
            assert False, "Ошибка в синтаксисе модели, не задан атрибут primaryKey или что-то еще"

        try:
            d = City.query.all()
            self.assertEqual(len(d), 10, msg="Не все данные вставились или не вставились")
        except Exception as e:
            self.fail(msg="Не верная модель")
