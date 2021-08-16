import json

def lambda_handler(event, context):
    message = "<!DOCTYPE html> <html> <head> <meta charset = \"UTF-8\" > </head> <body> Проверка 1, Проверка 2, Проверка 3 </body> </html>"
    print(message)
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }

lambda_handler(None, None)
