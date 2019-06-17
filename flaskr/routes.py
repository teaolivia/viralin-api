from models import models
from flask import request, make_response, jsonify
from flaskr import apis, sellers, promotors, contents, contentpromo, auth
from boto3.dynamodb.conditions import Key, Attr

@apis.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@apis.route('/bye')
def bye():
    return jsonify(sellers.creation_date_time)

@apis.route('/<seller_id>')
def henlo(seller_id):
    """
    Main menu, displaying login and register page of each user types.
    """
    response = sellers.get_item(
        Key={
            'seller_id': seller_id
        }
    )
    item = response['Item']
    return jsonify(item)

@apis.route('/<seller_id>/<promotor_id>/<content_id>', methods=['GET'])
def view_all():
    response = contentpromo.get_item(
            Key = {
                '_id': id
            }
        )
    item = response['Item']
    return jsonify(item)



