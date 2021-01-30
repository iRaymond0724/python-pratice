
# for flask connect to sqlite
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 設定資料庫位置，並建立 app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)

class Todo(db.Model):
    # __table__name = 'user_table'，若不寫則看 class name
    # 設定 primary_key
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80))

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<Todo %r>' % self.content


@app.route('/', methods=['GET'])
def hello():
    print("Total number of schools is", Todo.query.count())
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
