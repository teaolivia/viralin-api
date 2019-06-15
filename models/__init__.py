import boto3
from flaskr import apis

dbsession = boto3.Session(profile_name='admin-db')

# some useful modules
def kwargs_processor(**kwargs):
    for k, v in kwargs.items():
        print(f'Key={k} and Value={v}')