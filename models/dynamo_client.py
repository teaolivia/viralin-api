from models import dbsession


class ClientFactory:
    def __init__(self, client):
        dynamo_client = dbsession.client('dynamodb')

    def get_client(self):
        return self._client


class DynamoDBClient(ClientFactory):
    def __init__(self):
        super().__init__('dynamodb')