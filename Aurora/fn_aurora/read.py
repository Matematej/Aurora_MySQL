import boto3
import os
import json

rds_data = boto3.client('rds-data')
RDSclusterArn = os.environ["ClusterArn"]
SecretArn = os.environ["SecretArn"]
DBname = os.environ["DBname"]


def lambda_handler(event, context):
    decoded_event=json.loads(event['body'])
    TableName = decoded_event["TableName"]
    response = execute_statement('USE {DBname}; SELECT * FROM {TableName}')
    return response

def execute_statement(sql):
    response2 = rds_data.execute_statement(
        resourceArn = RDSclusterArn, 
        secretArn = SecretArn, 
        database = DBname, 
        sql = sql)