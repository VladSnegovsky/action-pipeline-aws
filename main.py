import json

def lambda_handler():
    message = 'Hello World!'
    print(message)
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }

lambda_handler()
# Test
