# JSON library for the output processing
import json

# datetime library for processing the epoch time to readable timestamp
import datetime

# AWS Lambda Handler
def lambda_handler(event, context):
    # Extact the user's input from the api URL path and store in arg variable
    arg = event['pathParameters']['arg']
    
    # Check if the User input is an Integer
    if arg.isdigit():
        print("User's input is an Integer ")

        # Check the lenght of User input epoch time to determine if it's in sec or ms.
        length = len(arg)
        
        # If the User input is in ms
        if length == 13:
            print("Given timestamp lenght is in milliseconds", length)
            s =  int(arg) / 1000.0
            #date_str = datetime.datetime.fromtimestamp(s).strftime('%d-%m-%Y %H:%M:%S.%f')
            output_message = datetime.datetime.fromtimestamp(s).ctime()

        # If the User input is in sec
        elif length == 10:
            print("Given timestamp lenght is in seconds", length)
            s =  int(arg)
            #date_str = datetime.datetime.fromtimestamp(s).strftime('%d-%m-%Y %H:%M:%S')
            output_message = datetime.datetime.fromtimestamp(s).ctime()
        
        # If the User input either not in ms or sec then return error
        else:
            print("User input doesn't look like an epoch time")
            output_message = "User's input doesn't look like an epoch time in seconds or milliseconds"
        
        
        body = {
            #"event": event,
            #"length": length,
            #"s": s,
            "Epoch Timestamp ": arg,
            "Input lenght ": length,
            "Readable Timestamp ": output_message
            }
    else:
        print("User input is string ")
        print("No.. input is not a number. It's a string")
        body = {
            "Epoch Timestamp ": arg,
            "Message": "User input is NOT an integer"
            }

    
    response = {
       "statusCode": 200,
       "headers": {
           "content-type": "application/json"
       },
       "body": json.dumps(body),
       "isBase64Encoded": False,
    }
    
    return response
