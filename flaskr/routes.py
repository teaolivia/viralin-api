from models import models
from flask import request, make_response, jsonify
from flaskr import apis, sellers, promotors, contents, contentpromo, auth
from boto3.dynamodb.conditions import Key, Attr
import json

@apis.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@apis.route('/bye')
def bye():
    return jsonify(sellers.creation_date_time)

@apis.route('/sellers/<seller_id>', methods=['GET'])
def get_sellers(seller_id):
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

@apis.route('/sellers/<seller_id>/promotors', methods=['GET'])
def get_sellers_promotors(seller_id):
    response = contentpromo.scan(
        FilterExpression=Attr('seller_id').eq(seller_id)
    )
    items = response['Items']
    data = json.load(items)
    promotors = []
    for field in data:  
        x = field['promotor_id'] 
        promotors.append(x)
    for i in promotors:
        promotor[i]
    return jsonify(promotors)
    # for i in items:
        # result = promotors.get_item(
        #     Key={
        #         'promotor_id': str(items[i])
        #     }
        # )
        # res = items[i]
        # # result['Item']
        # ans.append(res) 

@apis.route('/<seller_id>/<promotor_id>/<content_id>', methods=['GET'])
def get_content_through_seller_and_promotor(seller_id, promotor_id, content_id):
    response = contentpromo.scan(
        FilterExpression=Attr('seller_id').eq(seller_id) & Attr('promotor_id').eq(promotor_id)
                            & Attr('content_id').eq(content_id)
    )
    items = response['Items']
    return jsonify(items)



