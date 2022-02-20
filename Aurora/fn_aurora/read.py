import boto3
import os

rds_data = boto3.client('rds-data')
RDSclusterArn = os.environ["ClusterArn"]
SecretArn = os.environ["SecretArn"]
DBname = os.environ["DBname"]


def lambda_handler(event, context):
    TableName = event["TableName"]
    
    sql = f"""
        SELECT * FROM {TableName};
        """
    response = rds_data.execute_statement(
        resourceArn = RDSclusterArn, 
        secretArn = SecretArn, 
        database = DBname, 
        sql = sql)
    return response