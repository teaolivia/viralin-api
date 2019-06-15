#!flask/bin/python
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flaskr import apis, login, dynamo, sellers, promotors, contents
from flask import Flask, Blueprint, jsonify, request, abort, make_response
from flaskr.user import User
from bson.objectid import ObjectId
import json
import requests


class Sellers(User):
    def __init__(self, id, username, password):
        User.__init__(self, username, password)
        self.seller_id = id

    @apis.route('/sellers/login', methods=['POST'])
    def login():
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
        #return db.Promotors.count_documents({"seller_id": seller_id})
        pass

    @apis.route('/sellers', methods=['GET'])
    def get_sellers():
        response = sellers.get_item(
            Key={
                'seller_id': seller_id
                }
            )
        return jsonify({'results': response['Item']['sellers_value']})
        # seller_documents = [doc for doc in db.Sellers.find({})]
        # return jsonify({'sellers': seller_documents})

    @apis.route('/sellers/<seller_id>/<username>', methods=['GET'])
    def get_sellers_username(username):
        if username not in sellers:
            return "404 Not Found"
        return "return sellers username"

    @apis.route('/sellers/<seller_id>/promotors', methods=['GET'])
    def get_sellers_promotors():
        response = promotors.get_item(
            Key={
                'seller_id': seller_id
            }
        )
        item = response['Item']
        return item

    @apis.route('/sellers/<seller_id>/contents', methods=['GET'])
    def get_sellers_contents():
        response = contents.get_item(
            Key={
                'seller_id': seller_id
            }
        )
        item = response['Item']
        return item

    # counter which is displayed on dashboards
    @apis.route('/sellers/<seller_id>/total_active_contents', methods=['POST'])
    def count_active_contents(seller_id):
        response = contents.get_item(
            Key={
                'seller_id': seller_id,
                'status': True
            }
        )
        item = response['Item']
        return len(item)

    # count contents from a seller_id
    @apis.route('/sellers/<seller_id>/total_contents', methods=['POST'])
    def count_total_contents(seller_id):
        return jsonify(contents.item_count)

    # count total referral
    @apis.route('/sellers/<seller_id>/total_referrals', methods=['POST'])
    def count_referrals(seller_id):
        # return db.promotors.find({"seller_id": seller_id}).count()
        pass

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