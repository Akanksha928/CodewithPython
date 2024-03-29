from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

api_key = "TopSecret"
app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafe=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def find_cafe():
    location = request.args.get("loc")
    cafe_to_find = Cafe.query.filter_by(location=location).all()
    if cafe_to_find:
        return jsonify(cafe=[cafe.to_dict() for cafe in cafe_to_find])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


@app.route("/random")
def random():
    cafes = db.session.query(Cafe).all()
    random_cafe = choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(name=request.form.get("name"),
                    map_url=request.form.get("map_url"),
                    img_url=request.form.get("img_url"),
                    location=request.form.get("loc"),
                    has_sockets=bool(request.form.get("sockets")),
                    has_toilet=bool(request.form.get("toilet")),
                    has_wifi=bool(request.form.get("wifi")),
                    can_take_calls=bool(request.form.get("calls")),
                    seats=request.form.get("seats"),
                    coffee_price=request.form.get("coffee_price"),
                    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added to database."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_prices(cafe_id):
    cafe_to_be_updated = db.session.query(Cafe).get(cafe_id)
    if cafe_to_be_updated:
        cafe_to_be_updated.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(response={"error": "No such cafe ID."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    key = request.args.get("api-key")
    if key == api_key:
        cafe_to_delete = db.session.query(Cafe).get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted cafe from database."}), 200
        else:
            return jsonify(response={"error": "No such cafe ID."}), 404
    else:
        return jsonify(response={"error": "Not authorized."}), 403


if __name__ == '__main__':
    app.run(debug=True)
