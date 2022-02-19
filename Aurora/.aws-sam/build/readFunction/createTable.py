import boto3
import os
import json

rds_data = boto3.client('rds-data')
RDSclusterArn = os.environ["ClusterArn"]
SecretArn = os.environ["SecretArn"]
DBname = os.environ["DBname"]

TableName = {}

sql = """USE {DBname};
CREATE TABLE mbtiTable (
      name varchar(100) NOT NULL,
      mbti varchar(40) NOT NULL,
      PRIMARY KEY ( name ));"""
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