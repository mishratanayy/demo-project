from flask import Blueprint

# Create a blueprint for the API
api_bp = Blueprint('api', __name__)

from .hello import hello_route
