import json
import requests

def get_last_list():
    url = 'https://wm3ce6ayrl.execute-api.us-east-2.amazonaws.com/default/python-aws'
    response = requests.get(url, params=(), headers=())
    response = str(response.content.decode('utf8'))
    # response = response[1:-1]
    # list = response.split(",")
    # print(list)
    return response


def list_to_str(list):
    return str(list[0]) + ', ' + str(list[1]) + ', ' + str(list[2])


def lambda_handler(event, context):
    message = get_last_list()
    print(message)
    return {
        'statusCode': 200,
        'body': json.dumps(message, ensure_ascii=False)
    }

lambda_handler(None, None)
