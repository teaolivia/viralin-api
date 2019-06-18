#!flask/bin/python
from flaskr.user import User
from flaskr import apis, login, promotors, decimalencoder, contentpromo
from flask import Flask, jsonify, request, make_response
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from boto3.dynamodb.conditions import Key, Attr
import json
import requests

class Promotors(User):
    def __init__(self, id, username, password):
        self.__init__(self, username,password)
        self.id = promotor_id

    @apis.route('/<seller_id>/promotors', methods=['GET'])
    def view_all(seller_id):
        response = contentpromo.get_item(
            Key = {
                'seller_id': seller_id,
            }
        )
        item = response['Item']
        # for x in item:

        # response = table.scan(
        #     FilterExpression=Attr('promotor_id').lt(27)
        # )
        # items = response['Items']
        return jsonify(item['promotor_id'])

    @apis.route('/<promotor_id>/n_promotors', methods=['GET'])
    def n_promotors(promotor_id):
        response = contentpromo.scan(
            FilterExpression=Attr('promotor_id').eq(promotor_id)
        )
        item = response['Items']
        return jsonify("%d" % item)

    @apis.route('/contents/request/<content_id>', methods=['POST'])
    def send_request(self, content_id):
        # add new item to content-promo table
        pass
# # main driver
# if __name__ == '__main__':
#     app.run(port=5000,debug=True)