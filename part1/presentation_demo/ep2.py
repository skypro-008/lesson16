from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


# work with db

@app.route('/')
def get_users():
    # work with db
    return "OK"


if __name__ == '__main__':
    app.run(debug=True)