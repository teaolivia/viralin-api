import os, json, datetime
from bson.objectid import ObjectId
from flask import Flask, Blueprint, request
from flask_cors import CORS
from flask_dynamo import Dynamo
from flask_jwt_extended import JWTManager, create_access_token
from pymongo import MongoClient
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import boto3

apis = Flask(__name__)

## pymongo Config
client = MongoClient('mongodb://localhost:27017/')
db = client.viralinDB

## flask_dynamo
dynamo = Dynamo(apis)

## DynamoDB Config
# client
dbsession = boto3.Session(profile_name='admin-db')
dynamo_client = dbsession.client('dynamodb')
# resource
dynamo_resource = dbsession.resource('dynamodb')
sellers = dynamo_resource.Table('sellers')
promotors = dynamo_resource.Table('promotors')
contents = dynamo_resource.Table('contents')
contentpromo = dynamo_resource.Table('content-promotor')

## flask-JWT-extended
apis.debug = True
apis.config['JWT_SECRET_KEY'] = 'laskarkalong2019'
apis.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
jwt = JWTManager(apis)

## Flask-Login Config
login = LoginManager(apis)

## Flask-BCrypt Config
bcrypt = Bcrypt(apis)

## Flask-CORS Config
CORS(apis)

from flaskr import routes, user, sellers, promotors, contents