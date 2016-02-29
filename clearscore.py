#############################
## Clear scores in dynamodb table
## DRM 02/26/16
#############################
import boto3
import json
def lambda_handler(event, context):
    teams = ["A","B","C"]
    dynamo = boto3.resource('dynamodb').Table("testscore")
    for team in teams:
        response = dynamo.update_item(
            Key={
            'team' : team
            },
            UpdateExpression="set score = :val",
            ExpressionAttributeValues={
            ':val': 0
            }
        ) 
    retval = "Cleared Scores"
    return retval
