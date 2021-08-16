import json

def lambda_handler(event, context):
    message = "Проверка 1, Проверка 2, Проверка 3"
    print(message)
    return {
        'statusCode': 200,
        'body': json.dumps(message, ensure_ascii=False)
    }

lambda_handler(None, None)
