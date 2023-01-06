from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
# Подключение к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Flask_test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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


@app.route('/create-field', methods=['POST', 'GET'])
def create_field():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        
        field = Articles(title=title, intro=intro, text=text)
        try:
            db.session.add(field)
            db.session.commit()
            return redirect('/')
        except:
            "Упс... что-то пошло не так"
    else:
        return render_template('create-field.html')

def get_data_from_db():
    return Articles.query.order_by(Articles.date.desc()).all()[1].title

if __name__ == '__main__':
    app.run(debug=True)