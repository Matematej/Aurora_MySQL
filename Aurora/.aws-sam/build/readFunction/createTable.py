import boto3
import os
import json

rds_data = boto3.client('rds-data')
RDSclusterArn = os.environ["ClusterArn"]
SecretArn = os.environ["SecretArn"]
DBname = os.environ["DBname"]

sql = """USE {DBname};
CREATE TABLE {TableName} (
      name varchar(100) NOT NULL,
      mbti varchar(40) NOT NULL,
      PRIMARY KEY ( name ));"""
def lambda_handler(event, context):
    decoded_event=json.loads(event['body'])
    TableName = decoded_event["TableName"]
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