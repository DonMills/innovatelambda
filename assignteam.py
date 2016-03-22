import boto3

def teampick(number):
   if not number % 3:
       return "C"
   elif not number % 2:
       return "B"
   else:
       return "A"
def lambda_handler(event, context):
    dynamo = boto3.resource('dynamodb').Table("teamcount")
    response = dynamo.get_item(
    Key={
        'game': 'ripple'
        }
    )
    count = response["Item"]["teamcount"]
    teamval = teampick(count)
    dynamo.update_item(
        Key={
        'game': 'ripple'
        },
        UpdateExpression='SET teamcount = teamcount + :val',
        ExpressionAttributeValues={
        ':val': 1
        }
        )
    return teamval
