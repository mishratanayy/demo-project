from flask import Flask
from .routes import main_bp  # Import the main blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load configuration from config.py
    
    # Register blueprints
    app.register_blueprint(main_bp)
    
    return app
