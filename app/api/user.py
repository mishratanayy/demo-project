from flask import jsonify
from . import api_bp

@api_bp.route('/hello', methods=['GET'])
def hello_route():
    return jsonify({"message": "Hello, World!"})
