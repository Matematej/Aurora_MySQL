import boto3
import os
import json

rds_data = boto3.client('rds-data')
RDSclusterArn = os.environ["ClusterArn"]
SecretArn = os.environ["SecretArn"]
DBname = os.environ["DBname"]


def lambda_handler(event, context):
    TableName = event["TableName"]
    param1 = event["param1"]
    param2 = event["param2"]
    
    sql = f"""
        CREATE TABLE {TableName} (
         {param1} varchar(100) NOT NULL,
         {param2} varchar(40) NOT NULL,
        PRIMARY KEY ( {param1} ));
     """
    response = rds_data.execute_statement(
        resourceArn = RDSclusterArn, 
        secretArn = SecretArn, 
        database = DBname, 
        sql = sql)
    #print(response)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": response
        }),}