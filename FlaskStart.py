from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
# Подключение к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Flask_test.db'
db = SQLAlchemy(app)


# Создаем класс, где каждый объект - поле плоской таблице в базе данных
class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text(300), nullable=False)
    date = db.Column(db.DateTime(300), default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return '<Articles %r' % self.id
    

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f"User page: {name} with id {id}"


if __name__ == '__main__':
    app.run(debug=True)