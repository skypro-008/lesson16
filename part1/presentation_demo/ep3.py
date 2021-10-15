from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)


db.create_all()

jonh = User(id=1, name='jonh', age=30)
kate = User(id=2, name='kate', age=31)
max = User(id=3, name='max', age=32)

print(jonh.name, kate.name)

if __name__ == '__main__':
    app.run(debug=True)
