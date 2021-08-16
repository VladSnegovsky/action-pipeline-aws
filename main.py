import json
import requests


url = 'https://api.airtable.com/v0/appChbaVEmKqN2SS9/MainTable'
API = 'keyUXGosavkzeiGLV'


def get_min_max_id(response):
    min = response[0]["fields"]["ID"]
    max = response[0]["fields"]["ID"]
    for item in response:
        if item["fields"]["ID"] > max:
            max = item["fields"]["ID"]

        if item["fields"]["ID"] < min:
            min = item["fields"]["ID"]

    return min, max

def get_by_id(id, response):
    for item in response:
        if item["fields"]["ID"] == id:
            return item["fields"]["title"]
    return "error"


def delete_record(id):
    headers = {'Authorization': 'Bearer ' + API}
    requests.delete(url + '/' + str(id), params=(), headers=headers)


def get_data_n_id(response, id):
    for item in response:
        if item["fields"]["ID"] == id:
            return item["id"], item["fields"]
    return "error"


def add_record(record_data):
    headers = {'Authorization': 'Bearer ' + API,
               'Content-Type' : 'application/json'}
    data = {
      "records": [
        {
          "fields": record_data
        }
      ]
    }
    requests.post(url, json=data, headers=headers)


def get_message():
    headers = {'Authorization': 'Bearer ' + API}

    response = requests.get(url, params=(), headers=headers)        # get response
    response = json.loads(response.content.decode('utf8'))          # response to json
    response = response["records"]          # get all records from json file

    min, max = get_min_max_id(response)
    message = str(get_by_id(min, response))
    message = message + ", " + str(get_by_id(min+1, response))
    message = message + ", " + str(get_by_id(min+2, response))

    first_record_id, first_record_data = get_data_n_id(response, min)

    delete_record(first_record_id)
    first_record_data["ID"] = max+1
    add_record(first_record_data)

    return message


get_message()


def lambda_handler(event, context):
    message = get_message()

    print(message)
    return {
        'statusCode': 200,
        'body': json.dumps(message, ensure_ascii=False)
    }

lambda_handler(None, None)
