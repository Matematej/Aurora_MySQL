import boto3
import os
import json

rds_data = boto3.client('rds-data')
RDSclusterArn = os.environ["ClusterArn"]
SecretArn = os.environ["SecretArn"]
DBname = os.environ["DBname"]

name={}
mbti={}
TableName = {}

sql = """USE {DBname};
INSERT INTO mbtiTable (name, mbti)
VALUES ('saber', 'intj');"""

def lambda_handler(event, context):
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