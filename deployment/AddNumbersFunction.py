def lambda_handler(event, context):
    number1 = event.get('number1', 0)
    number2 = event.get('number2', 0)

    result = number1 + number2

    return {
        'statusCode': 200,
        'body': {
            'sum': result
        }
    }
