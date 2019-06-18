#!flask/bin/python
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flaskr import apis, login, dynamo, sellers, contentpromo, promotors, contents, decimalencoder, dynamo_client
from flask import Flask, Blueprint, jsonify, request, abort, make_response
from flaskr.user import User
from bson.objectid import ObjectId
from boto3.dynamodb.conditions import Key, Attr
import json
import requests


class Sellers(User):
    def __init__(self, id, username, password):
        User.__init__(self, username, password)
        self.seller_id = self.generate_id()

    def generate_id(self):
        n = sellers.item_count()
        it = [int(s) for s in seller_id.split() if s.isdigit()]
        return "seller" + str(it + 1)

    @apis.route('/sellers/login', methods=['GET','POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        self.username = request.json.get('username', None)
        self.password = self.check_password_hash(request.json.get('password', None))
        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400
        if username != 'test' or password != 'test':
            return jsonify({"msg": "Bad username or password"}), 401
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    @apis.route('/sellers/register/', methods=['GET','POST'])
    def sign_up():
        business_name = request.form.get('namaUsaha', None)
        business_type = request.form.get('jenisUsaha', None)
        name = request.form.get('namaPebisnis', None)
        email = request.form.get('email', None)
        phone = request.form.get('nomorTelepon', None)
        alamat = request.form.get('alamat', None)
        birthplace = request.form.get('tempatLahir', None)
        birthdate = request.form.get('tanggalLahir', None)
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        phash = bcrypt.generate_password_hash(password).decode('utf-8')
        obj = {
            'seller_id': request.json['seller_id']
            'email' : request.json['email'],
            'password' : request.json['password'],
            'business_name': request.json['business_name'],
        }
        sellers.put_item(obj)

    def upload_profile_picture(self, seller_id):
        pass
    
    # basic getter route
    @apis.route('/sellers/<seller_id>/n_promotors', methods=['GET'])
    def count_total_promotors(self, seller_id):
        print(promotors.item_count)
        pass

    # @apis.route('/sellers/<seller_id>', methods=['GET'])
    # def get_sellers(seller_id):
    #     response = sellers.get_item(
    #         Key={
    #             'seller_id': seller_id
    #         }
    #     )
    #     item = response['Item']
    #     return jsonify(item)

    # @apis.route('/sellers/<seller_id>/promotors', methods=['GET'])
    # def get_sellers_promotors(seller_id):
    #     response = dynamo_client.get_item(
    #         TableName='promotors',
    #         Key={
    #             'seller_id': seller_id
    #         }
    #     )
    #     item = response['Item']
    #     return jsonify(item)

    @apis.route('/sellers/<seller_id>/contents', methods=['GET'])
    def get_sellers_contents():
        response = contents.get_item(
            Key={
                'seller_id': seller_id
            }
        )
        item = response['Item']
        return jsonify(item)

    # counter which is displayed on dashboards
    @apis.route('/sellers/<seller_id>/total_active_contents', methods=['POST'])
    def count_active_contents(seller_id):
        response = contentpromo.scan(
            FilterExpression=Attr('seller_id').eq(seller_id)
        )
        seller = response['Item']
        for s in seller:
            contents = contents_id
            result = contents.scan(
                FilterExpression = Attr('content_id').eq(s['content_id']) & Attr('status').eq(True)
            )
        res = result['Item']
        return len(res)

    # count contents from a seller_id
    @apis.route('/sellers/<seller_id>/total_contents', methods=['POST'])
    def count_total_contents(seller_id):
        response = contentpromo.scan(
            FilterExpression=Attr('seller_id').eq(seller_id)
        )
        item = response['Items'].decode('utf-8')
        return jsonify(len(item))

    # count total referral
    @apis.route('/sellers/<seller_id>/total_referrals', methods=['POST'])
    def count_referrals(seller_id):
        response = contentpromo.scan(
            FilterExpression=Attr('seller_id').eq(seller_id)
        )
        item = response['Items'].decode('utf-8')
        return jsonify(item)

    @apis.route('/sellers/<string:seller_id>/stats/', methods=['GET'])
    def view_stats(seller_id):
        response = sellers.get_item(
            Key={
                'seller_id': seller_id
            }
        )
        item = response['Item'].decode('utf-8')
        return item

# # main driver
# if __name__ == '__main__':
#     app.run(port=5001,debug=True)