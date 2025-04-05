
import boto3
import json
import gzip
import base64
from datetime import datetime

s3 = boto3.client('s3')
bucket_name = 'user-activity-processed-data'

def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        data = json.loads(payload)

        now = datetime.utcnow()
        prefix = now.strftime("user-events/%Y-%m-%d/")
        filename = now.strftime("%H-%M-%S-%f.json")
        key = prefix + filename

        s3.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=json.dumps(data).encode('utf-8')
        )

    return {'statusCode': 200, 'body': 'Success'}
