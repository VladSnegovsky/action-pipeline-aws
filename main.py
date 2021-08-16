import json

def lambda_handler(event, context):
    msg = "Проверка 1, Проверка 2, Проверка 3"
    print(msg)
    return {
        'statusCode': 200,
        'body': json.dumps(msg, ensure_ascii=False)
    }

lambda_handler(None, None)
