import boto3

def lambda_handler(event, context):
    dynamo = boto3.resource('dynamodb').Table("teamcount")
    response = dynamo.get_item(
    Key={
        'game': 'ripple'
        }
    )
    count = response["Item"]["teamcount"]
    return count - 1
