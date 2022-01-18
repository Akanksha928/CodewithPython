from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-10-movies.db"
db = SQLAlchemy(app)
api_key = '47fbb47f817a8c592344539e411d29ec'


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=True)
    year = db.Column(db.Integer, unique=False, nullable=True)
    description = db.Column(db.String(1000), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(1000), nullable=True)
    img_url = db.Column(db.String(1000), nullable=True)


db.create_all()


class Form(FlaskForm):
    new_rating = FloatField(label='Your rating out of 10: ', validators=[DataRequired()])
    new_review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Submit Changes')


class Add(FlaskForm):
    new_movie = StringField(label='Enter Movie Name:', validators=[DataRequired()])
    submit = SubmitField("Add Movie")


neww_movie = Movies(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

# db.session.add(neww_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movies.query.order_by(Movies.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", data=all_movies)


@app.route('/update', methods=['POST', 'GET'])
def update():
    form = Form()
    if form.validate_on_submit():
        movie_id = request.args.get('id')
        movie_to_update = Movies.query.get(movie_id)
        movie_to_update.rating = float(form.new_rating.data)
        movie_to_update.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movies.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['POST', 'GET'])
def add():
    form = Add()
    if form.validate_on_submit():
        movie_title = form.new_movie.data
        parameters = {"api_key": api_key,
                      "query": movie_title}
        response = requests.get(url="https://api.themoviedb.org/3/search/movie", params=parameters)
        data = response.json()['results']
        return render_template('select.html', data=data)
    return render_template('add.html', form=form)


@app.route('/find')
def find_movie():
    movie_id = request.args.get('id')
    parameters = {"api_key": api_key, }
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}", params=parameters)
    data = response.json()
    new_movie = Movies(title=data['original_title'], img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}", description=data['overview'], year=data['release_date'].split('-')[0])
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('update', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
