import boto3
import json
import time
import logging

dynamodb = boto3.resource('dynamodb')

def update(event, context):
    if 'postId' not in event['pathParameters']:
        logging.error("Validation Failed")
        raise Exception("Couldn't delete the item.")

    data = json.loads(event['body'])
    
    timestamp = str(time.time())

    table = dynamodb.Table('postTable')

    table.update_item(
        Key = {
            'postId': event['pathParameters']['postId']
        },
        UpdateExpression='SET textTodo = :t, '
                         'favorite = :f, '
                         'updatedAt = :u',

        ExpressionAttributeValues={
            ':t': data['textTodo'],
            ':f': data['favorite'],
            ':u': timestamp
        },
        ReturnValues="UPDATED_NEW"
    )

    response = {
        "statusCode": 200,
        "headers" : {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }
    }

    return response