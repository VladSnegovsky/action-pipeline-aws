import json

def lambda_handler():
    message = 'Hello AWS!'
    print(message)
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }

lambda_handler()