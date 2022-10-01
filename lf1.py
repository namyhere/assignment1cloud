import json
import datetime

def lambda_handler(event, context):
    return {
        'status' : 'success',
        'status_code' : 200,
        'messages':
         [
            {
                "type":"unstructured",
                "unstructured": {
                    "id":"1",
                    "text": "Application under development. Search functionality will be implemented in Assignment 2",
                    "timestamp": str(datetime.datetime.now().timestamp())
                }
            }
        ],
        'headers' : {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        }
    }