from flask import Flask, jsonify
import os

def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev', 
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def hello_world():
        return jsonify({ "message": "Hello world!"})
    
    @app.route('/smiley')
    def smiley():
        return ':)'

    return app





