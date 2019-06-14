from models import models
from flask import request, make_response, jsonify
from flaskr import apis, sellers

@apis.route('/')
def henlo():
    """
    Main menu, displaying login and register page of each user types.
    """
    return 'henlo'

@apis.route('/bye')
def bye():
    return jsonify(sellers.creation_date_time)

@apis.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)