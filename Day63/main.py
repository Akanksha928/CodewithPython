from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    return render_template('index.html', data=all_books)


@app.route('/edit', methods=['POST', 'GET'])
def editing():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Books.query.get(book_id)
        book_to_update.rating = request.form["editing"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    selected_book = Books.query.get(book_id)
    return render_template('editing.html', book=selected_book)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        new_book = Books(title=request.form['name'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

