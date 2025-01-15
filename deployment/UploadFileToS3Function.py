import boto3  # boto3 package for aws connection to code
import base64
import json
import os

# connection setup
s3 = boto3.client('s3')

def lambda_handler(event, context):
    file_content = event['file_content']
    file_name = event['file_name']
    bucket_name = os.environ['YOUR_BUCKET_NAME']

    decoded_file = base64.b64decode(file_content)

    s3.put_object(Bucket=bucket_name, Key=file_name, Body=decoded_file)

    return {
        'statusCode': 200,
        'body': json.dumps(f"File {file_name} uploaded to {bucket_name}.")
    }
