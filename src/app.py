"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,Planet,People,Favorites_people,Favorites_planets



app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/users', methods=['GET'])
def handle_hello():
    all_users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), all_users))
    response_body = all_users
    return jsonify(response_body),200
   


# Metodos para People
@app.route('/people', methods=['GET', 'POST'])
def handle_people():
    if request.method == 'POST':  
        body = request.get_json()
        character = People(
            name= body["name"],
            description = body["description"],
            height = body["height"]
        )
        db.session.add(character)
        db.session.commit()

        response_body = {
        "msg": "Hello, POST send"
        }
        return jsonify(response_body), 200
        
    if request.method=='GET':
        all_people = People.query.all()
        all_people = list(map(lambda x: x.serialize_people(), all_people))
        response_body = all_people
        return jsonify(response_body),200


@app.route('/people/<int:id>', methods=['GET','PUT','DELETE'])
def handle_detailed_people(id):
    if request.method == 'GET':
        character = People.query.get(id)
        return jsonify(character.serialize_people()), 200
    
    if request.method == 'PUT':
        body = request.get_json()
        character = People.query.get(id)
        character.name = body["name"]
        character.description = body["description"]
        character.height = body["height"]
        db.session.commit()
        return jsonify(character.serialize_people()), 200

    if request.method == 'DELETE':
        character = People.query.get(id)
        db.session.delete(character)
        db.session.commit()
        return jsonify({"message":"character deleted"}),200
        

#Metodos para planet
@app.route('/planet', methods=['GET', 'POST'])
def handle_planet():
    if request.method == 'POST':
        body = request.get_json()
        new_planet = Planet(
            name= body["name"],
            description = body["description"],
            diameter = body["diameter"]
        )
        db.session.add(new_planet)
        db.session.commit()
        
        response_body = {
        "msg": "Hello, POST send"
        }

        return jsonify(response_body), 200
        
    if request.method=='GET':
        all_planet = Planet.query.all()
        all_planet = list(map(lambda x: x.serialize_planet(), all_planet))
        response_body = all_planet
        return jsonify(response_body),200


@app.route('/planet/<int:id>',methods=['GET','PUT','DELETE'])
def handle_detailed_planet(id):
    if request.method == 'GET':
        detailed_planet = Planet.query.get(id)
        return jsonify(detailed_planet.serialize_planet(),200)

    if request.method == 'PUT':
        body = request.get_json()
        detailed_planet = Planet.query.get(id)
        detailed_planet.name = body["name"]
        detailed_planet.description = body["description"]
        detailed_planet.height = body["diameter"]
        db.session.commit()
        return jsonify(detailed_planet.serialize_planet()), 200

    if request.method == 'DELETE':
        favorite_planet = Favorites_planets.query.filter_by(planet_id =id)
        favorite_planet = list(map(lambda x: x.serialize_favorites_planets(), favorite_planet))
        # favorite_planet.planet_id = id
        # favorite_planet = Favorites_planets.query.filter_by(planet_id =id)
        # favorite_planet = list(map(lambda x: x.serialize_favorites_planets(), favorite_planet))
        # favorite_planet = favorite_planet.planet_id
        db.session.delete(favorite_planet)
        db.session.commit()
        planet = Planet.query.get(id)
        db.session.delete(planet)
        # planet = Planet.query.get(id)
        # db.session.delete(planet)
        # # favorite_planet = Favorites_planets.query.filter(Favorites_planets.planet_id ==id)
        # # favorite_planet = list(map(lambda x: x.serialize_favorites_planets(), favorite_planet))
        # # db.session.delete(planet,favorite_planet[id])
        db.session.commit()
        return jsonify({"message":"planet deleted"}),200



#Favorites
@app.route('/users/favorites')
def handle_favorites():
    all_favorites = []

    all_favorites_people = Favorites_people.query.all()
    all_favorites_people = list(map(lambda x: x.serialize_favorites_people(), all_favorites_people))
    all_favorites.append(all_favorites_people)

    all_favorites_planets = Favorites_planets.query.all()
    all_favorites_planets = list(map(lambda x: x.serialize_favorites_planets(), all_favorites_planets))
    all_favorites.append(all_favorites_planets)

    return jsonify(all_favorites),200

    
    
@app.route('/user/<int:user_id>/favorite/people/<int:people_id>', methods=['POST'])
def handle_people_favorites(user_id,people_id):
    favorite_people = Favorites_people(
        user_id = user_id,
        character_id = people_id
    )
    db.session.add(favorite_people)
    db.session.commit()

    response_body = {
    "msg": "Hello, POST send"
    }
    return jsonify(response_body), 200


@app.route('/user/<int:user_id>/favorite/planet/<int:planet_id>', methods=['POST'])
def handle_planet_favorites(user_id,planet_id):
    favorite_planet = Favorites_planets(
        user_id = user_id,
        planet_id = planet_id
    )
    db.session.add(favorite_planet)
    db.session.commit()

    response_body = {
    "msg": "Hello, POST send"
    }
    return jsonify(response_body), 200




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
