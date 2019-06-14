import decimal
import json

from models import dbsession, kwargs_processor
from models.dynamo_client import DynamoDBClient
from models.dynamodb import DynamoDB

def get_dynamodb_resource():
    dynamodb = dbsession.resource("dynamodb", region_name="ap-southeast-1")
    """ :type : pyboto3.dynamodb """
    return dynamodb

def get_dynamodb():
    dynamodb_client = DynamoDBClient().get_client()
    dynamodb = DynamoDB(dynamodb_client)
    return dynamodb

def get_item_on_table(table_name, field, field_value):
    try:
        response = get_dynamodb_resource().Table(table_name).get_item(
            Key= {
                field: field_value
            }
        )
    except ClientError as error:
        print(error.response['Error']['Message'])
    else:
        item = response['Item']
        print("Got the item successfully!")
        print(str(response))

def put_item_on_table(table_name, field, field_value):
    try:
        response = get_dynamodb_resource().Table(table_name).put_item(
            Item= {
                field: field_value
            }
        )
        print("A New Post added to the collection successfully!")
        print(str(response))
    except Exception as error:
        print(error)

def delete_item_on_table(table_name, field, field_value):
    try:
        response = get_dynamodb_resource().Table(table_name).delete_item(
            Key= {
                    field: field_value
                }
            )
    except ClientError as error:
        if error.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(error.response['Error']['Message'])
        else:
            raise
    else:
        print("Deleted item successfully!")
        print(str(response))