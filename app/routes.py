from flask import Blueprint

# Create the Blueprint for general routes
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return 'Welcome to the Flask App!'

@main_bp.route('/version')
def about():
    return {"version":"v1"}
