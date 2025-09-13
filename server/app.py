from flask import Flask, jsonify
from flask_migrate import Migrate 
from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

migrate = Migrate(app, db)
db.init_app(app)

@app.route("/earthquakes/<int:id>")
def get_earthquake(id):
    quake = Earthquake.query.get(id)
    if quake:
        return jsonify(quake.to_dict()), 200
    return jsonify({"message": f"Earthquake {id} not found."}), 404

@app.route("/earthquakes/magnitude/<float:magnitude>")
def get_earthquakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    return jsonify({
        "count": len(quakes),
        "quakes": [q.to_dict() for q in quakes]
    }), 200 