import json

def lambda_handler(event, context):
    message = "<meta charset=\"UTF-8\"> Проверка 1, Проверка 2, Проверка 3"
    print(message)
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }

lambda_handler(None, None)
