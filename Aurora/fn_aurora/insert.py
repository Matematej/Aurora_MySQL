import boto3
import os
import json

rds_data = boto3.client('rds-data')
RDSclusterArn = os.environ["ClusterArn"]
SecretArn = os.environ["SecretArn"]
DBname = os.environ["DBname"]

def lambda_handler(event, context):
    TableName = event["TableName"]
    Name = event["Name"]
    MBTI = event["MBTI"]
    sql = f"""INSERT INTO {TableName} (name, mbti)
    VALUES ('{Name}', '{MBTI}');"""
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