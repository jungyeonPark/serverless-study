import boto3
import json
import uuid
import time

dynamodb = boto3.resource('dynamodb')

def create(event, context):
    data = json.loads(event['body'])

    timestamp = str(time.time())

    table = dynamodb.Table('postTable')

    item = {
        'postId': str(uuid.uuid1()),
        'postedAt': timestamp,
        'textTodo': data['textTodo'] 
    }

    table.put_item(Item=item)

    response = {
        "statusCode": 200,
        "headers" : {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps(item)
    }
    return response