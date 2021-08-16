import json
import requests

def lambda_handler(event, context):
    url = 'https://wm3ce6ayrl.execute-api.us-east-2.amazonaws.com/default/python-aws'
    response = requests.get(url, params=(), headers=())
    message = "Проверка 1, Проверка 2, Проверка 3"
    print(message)
    return {
        'statusCode': 200,
        'body': json.dumps(message, ensure_ascii=False)
    }

lambda_handler(None, None)
