from flask import Flask
from flask_cors import CORS
from .routes import main_bp  # Import the main blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load configuration from config.py
    print("Hello creating flask app")
    # Register blueprints
    app.register_blueprint(main_bp)
    CORS(app)
    return app
