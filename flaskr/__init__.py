import os, json, datetime
from bson.objectid import ObjectId
from flask import Flask, Blueprint, request
from flask_cors import CORS
from flask_dynamo import Dynamo
from flask_jwt_extended import JWTManager, create_access_token
#from pymongo import MongoClient
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
import boto3

apis = Flask(__name__)
auth = HTTPBasicAuth()

## pymongo Config
# client = MongoClient('mongodb://localhost:27017/')
# db = client.viralinDB

## flask_dynamo
dynamo = Dynamo(apis)

## DynamoDB Config
# client
dbsession = boto3.Session(profile_name='admin-db')
dynamo_client = dbsession.client('dynamodb')
# # resource
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

## Flask-Cognito Config
# configuration
apis.config.extend({
    'COGNITO_REGION': 'ap-southeast-1,
    'COGNITO_USERPOOL_ID': 'ap-southeast-1',

    # optional
    'COGNITO_APP_CLIENT_ID': '256a3d3ett1nsfrasp0r4vrsk8',  # client ID you wish to verify user is authenticated against
    'COGNITO_CHECK_TOKEN_EXPIRATION': False,  # disable token expiration checking for testing purposes
    'COGNITO_JWT_HEADER_NAME': 'X-MyApp-Authorization',
    'COGNITO_JWT_HEADER_PREFIX': 'Bearer',
})


# initialize extension
cogauth = CognitoAuth(app)

@cogauth.identity_handler
def lookup_cognito_user(payload):
    """Look up user in our database from Cognito JWT payload."""
    return User.query.filter(User.cognito_username == payload['username']).one_or_none()

from flaskr import routes, user, sellers, promotors, contents