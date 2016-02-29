##############################
## Increment a score in dynamodb table
## DRM 02/26/16
##############################
import boto3
import json
def lambda_handler(event, context):
    teams = ["A","B","C"]
    dynamo = boto3.resource('dynamodb').Table("testscore")
    if event['team'] in teams:
        response = dynamo.update_item(
        Key={
            'team' : event['team']
            },
        UpdateExpression="set score = score + :val",
        ExpressionAttributeValues={
            ':val': 1
            }
        )
        retval = "Added one to team " + event["team"]
    else:
        retval = "No such team - must be A, B, or C"
    return retval
