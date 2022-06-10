from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import os

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app) # basic initialization

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
        return ':)'

    return app





