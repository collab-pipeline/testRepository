import json
#import os
#import boto3
#import logging
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps('Hello from Lambda!!')
    }