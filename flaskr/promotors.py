#!flask/bin/python
from flaskr.user import User
from flaskr import apis, login, promotors, decimalencoder
from flask import Flask, jsonify, request, make_response
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import json
import requests

class Promotors(User):
    def __init__(self, id, username, password):
        self.__init__(self, username,password)
        self.id = promotor_id

    @apis.route('/promotors', methods=['GET'])
    def view_all():
        response = promotors.get_item(
                Key = {
                    'promo': name
                }
            )
        item = response['Item']
        return jsonify(item)

    @apis.route('/<seller_id>/n_promotors', methods=['GET'])
    def n_promotors():
        return json.dumps(promotors.item_count())

    @apis.route('/contents/request/<content_id>', methods=['POST'])
    def send_request(self, content_id):
        # add new item to content-promo table
        pass
# # main driver
# if __name__ == '__main__':
#     app.run(port=5000,debug=True)