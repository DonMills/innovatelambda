#######################################
## Check score in dynamodb table
## DRM 02/26/16
#######################################

import boto3
import json
def lambda_handler(event, context):
    dynamo = boto3.resource('dynamodb').Table("testscore")
    response = dynamo.scan()
    return response['Items']
