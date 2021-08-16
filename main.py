import json
import requests


def get_list():
    list = get_last_list()      # get last list

    name = 'MainTable'                  # name of the table
    app_id = 'appbf4PvPrAWaFeY5'        # id of app
    url = 'https://api.airtable.com/v0/' + app_id + '/' + name      # link to the table

    API = 'keyUXGosavkzeiGLV'       # id of the user
    headers = {'Authorization': 'Bearer ' + API}

    response = requests.get(url, params=(), headers=headers)        # get response
    response = json.loads(response.content.decode('utf8'))          # response to json
    response = response["records"]          # get all records from json file
    # print(response)  # check result

    first_title = response[0]['fields']['title']        # get first title
    second_title = response[1]['fields']['title']       # get second title
    third_title = response[2]['fields']['title']        # get third title

    coincidences = 0
    amount = len(response)

    for index, item in enumerate(response):           # create list from all titles
        amount -= 1

        if list[coincidences].strip() == item["fields"]["title"].strip():
            # here we count the number of coincidences
            coincidences += 1
        else:
            print(str(list[coincidences]) + " != " + str(item["fields"]["title"]))
            # if current item does not match the desired item in the list - it was a single coincidence
            # and this isn't a necessary coincidences
            coincidences = 0

        if coincidences == 3 and amount == 0:
            # case when the last element will be the first in the list
            list.pop(0)
            list.append(first_title)
            break
        elif coincidences == 3 and amount > 0:
            # case when the last element will be next in list
            list.pop(0)
            item = response[index+1]
            list.append(item["fields"]["title"])
            break

    if coincidences == 2:
        # if there were 2 coincidences, then the last will be first item in list
        # then we delete first and second, then first and second elements of the list append to the end
        list.pop(0)
        list.pop(1)
        list.append(first_title)
        list.append(second_title)
    elif coincidences == 1:
        # if there were 1 coincidence, then we clear all the list and take 3 first items
        list.pop(0)
        list.pop(0)
        list.pop(0)
        list.append(first_title)
        list.append(second_title)
        list.append(third_title)

    return list


def get_last_list():
    url = 'https://wm3ce6ayrl.execute-api.us-east-2.amazonaws.com/default/python-aws'
    response = requests.get(url, params=(), headers=())
    response = str(response.content.decode('utf8'))
    response = response[1:-1]
    list = response.split(",")
    # print(list)
    return list


def list_to_str(list):
    return str(list[0]) + ', ' + str(list[1]) + ', ' + str(list[2])


def lambda_handler(event, context):
    message = list_to_str(get_list())
    print(message)
    return {
        'statusCode': 200,
        'body': json.dumps(message, ensure_ascii=False)
    }

lambda_handler(None, None)
