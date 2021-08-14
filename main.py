import json

def lambda_handler(event, context):
    message = "Hello AWS!"
    print(message)
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }

lambda_handler(None, None)
