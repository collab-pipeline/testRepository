import json
import os
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
client = boto3.client('ecs')

def lambda_handler_(event, context):
    update_service(os.environ.get("cluster"), os.environ.get("service_name"))
    return {
        "statusCode": 200,
        "body": json.dumps('Hello from Lambda!!')
    }
