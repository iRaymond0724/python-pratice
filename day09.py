"""

# for flask connect to sqlite
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# @app.route('/', methods=['GET'])
# def index():
#     return 'Hello Geeks ! '

if __name__ == '__main__':
    app.run()

"""

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://iraymond:111111@localhost:3306/test"


mysql = SQLAlchemy()
mysql.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']

        query_data = mysql.engine.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        print(query_data)
        return 'success'
    return 'fail'


if __name__ == '__main__':
    app.run()