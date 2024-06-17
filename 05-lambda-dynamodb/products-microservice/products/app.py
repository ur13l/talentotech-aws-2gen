import json
import boto3
import os 
import uuid

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):

    table = dynamodb.Table(os.environ['TABLE_NAME'])
    resource = event.get('resource', '/')
    body = json.loads(event.get('body', '{}'))

    if resource == '/products/create':
        body['id'] = str(uuid.uuid4())
        response = table.put_item(Item=body)
        return {
            "statusCode": 200,
            "body": json.dumps(response),
        }
   
    return {
        "statusCode": 404,
        "body": json.dumps({
            "message": "Not found",
        }),
    }
