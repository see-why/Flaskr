from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin
from models import setup_db, Plant
import os

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app) # basic initialization
    setup_db(app)
    # CORS(app, resources={r"*/api/*": { "origins": '*' }}) more specific initialization

    app.config.from_mapping(
        SECRET_KEY='dev', 
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers","Content-Type, Authorization")
        response.headers.add("Access-Control-Allow-Methods","GET, POST, PATCH, DELETE, OPTIONS")
        return response

    @app.route('/')
    def hello_world():
        return jsonify({ "message": "Hello world!"})
    
    @app.route('/smiley')
    @cross_origin
    def smiley():
        return jsonify({ "message": ":)"})

    @app.route('/plants', methods=['GET','POST'])
    #@cross_origin
    def get_plants():
        # Implement pagination
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * 10
        end = start + 10

        plants = Plant.query.all()
        formatted_plants = [plant.format() for plant in plants]
        return jsonify({
            'success': True,
            'plants':formatted_plants[start:end],
            'total_plants':len(formatted_plants)
            })

    @app.route('/plants/<int:plant_id>')
    def get_specific_plant(plant_id):
        plant = Plant.query.filter(Plant.id==plant_id).one_or_none()
        if plant is None:
            abort(404)
        else:   
            return jsonify({
                'success': True,
                'plant': plant.format()
            })

    return app





