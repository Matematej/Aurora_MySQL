import boto3
import os
import json

rds_data = boto3.client('rds-data')
RDSclusterArn = os.environ["ClusterArn"]
SecretArn = os.environ["SecretArn"]
DBname = os.environ["DBname"]

sql = """USE {DBname};
INSERT INTO {TableName} (name, mbti)
VALUES ('{Name}', '{MBTI}');"""

def lambda_handler(event, context):
    decoded_event=json.loads(event['body'])
    TableName = decoded_event["TableName"]
    Name = decoded_event["Name"]
    MBTI = decoded_event["MBTI"]
    response = rds_data.execute_statement(
        resourceArn = RDSclusterArn, 
        secretArn = SecretArn, 
        database = DBname, 
        sql = sql)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": response
        }),}