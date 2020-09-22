import boto3
import json
import logging

dynamodb = boto3.resource('dynamodb')

def delete(event, context):
    # data = json.loads(event['body'])
    if 'postId' not in event['pathParameters']:
        logging.error("Validation Failed")
        raise Exception("Couldn't delete the item.")

    table = dynamodb.Table('postTable')

    table.delete_item(
        Key = {
            'postId': event['pathParameters']['postId']
        }
    )
    print(event['pathParameters'])

    response = {
        "statusCode": 200,
        "headers" : {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }
    }

    return response