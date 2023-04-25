from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from waitress import serve

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<article {self.id}>'


@app.route('/')
def index():
    return render_template('index.html', title="Interns")


@app.route('/biography')
def biography():
    return render_template('biography.html', title="О себе")


@app.route('/experience')
def experience():
    return render_template('experience.html', title='Опыт')


@app.route('/reviews')
def reviews():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('reviews.html', articles=articles, title='Истории')


@app.route('/reviews/<int:id>')
def review_detail(id):
    articles = Article.query.get(id)
    return render_template('review_detail.html', articles=articles)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/reviews')
        except:
            return "Ошибка"
    else:
        return render_template('create.html', title='Создание отзыва')


@app.route('/enter')
def enter():
    return render_template('enter.html')


if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=5000)
    serve(app, host="127.0.0.1", port=5000)

