from flask import Flask, jsonify, request
from flask_migrate import Migrate

# Import models with fallback for different import contexts
try:
    from models import db, Hero, Power, HeroPower
except ImportError:
    from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
Migrate(app, db)

# ======= SERIALIZERS =======
def serialize_power(p):
    if not p:
        return None
    return {"id": p.id, "name": p.name, "description": getattr(p, "description", None)}

def serialize_hero_power(hp):
    return {
        "id": hp.id,
        "hero_id": hp.hero_id,
        "power_id": hp.power_id,
        "strength": hp.strength,
        "power": serialize_power(getattr(hp, "power", None))
    }

def serialize_hero(h):
    return {
        "id": h.id,
        "name": h.name,
        "super_name": getattr(h, "super_name", None),
        "hero_powers": [serialize_hero_power(hp) for hp in getattr(h, "hero_powers", [])]
    }

# ======= ROUTES =======
@app.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([serialize_hero(h) for h in heroes]), 200

@app.route("/heroes/<int:id>", methods=["GET"])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(serialize_hero(hero)), 200

@app.route("/powers", methods=["GET"])
def get_powers():
    powers = Power.query.all()
    return jsonify([serialize_power(p) for p in powers]), 200

@app.route("/powers/<int:id>", methods=["GET"])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(serialize_power(power)), 200

@app.route("/powers/<int:id>", methods=["PATCH"])
def patch_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    data = request.get_json(silent=True) or {}
    try:
        if "description" in data:
            power.description = data["description"]
        db.session.commit()
        return jsonify(serialize_power(power)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 422

@app.route("/hero_powers", methods=["POST"])
def add_hero_power():
    data = request.get_json() or {}
    try:
        hp = HeroPower(
            strength=data["strength"],
            hero_id=data["hero_id"],
            power_id=data["power_id"]
        )
        db.session.add(hp)
        db.session.commit()
        return jsonify(serialize_hero_power(hp)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 422


if __name__ == "__main__":
    app.run(debug=True, port=5555)