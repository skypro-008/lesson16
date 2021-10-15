import unittest

import sqlalchemy


class TestCase(unittest.TestCase):
    def test(self):
        try:
            from task import Author, Book
        except ImportError:
            self.fail("Не правильное имя класса Author, Book")
        except sqlalchemy.exc.ArgumentError:
            self.fail("Ошибка в синтаксисе модели, не задан атрибут primaryKey или что-то еще")
        try:
            from task import db
        except ImportError:
            self.fail("Отсутствует переменная db, которая была изначально")

        db.drop_all()
        db.create_all()

        author = Author(id=1, first_name='name', last_name="spec")
        book = Book(id=1, title='name', copyright=1, author_id=1)

        with db.session.begin():
            db.session.add(author)
        with db.session.begin():
            db.session.add(book)
