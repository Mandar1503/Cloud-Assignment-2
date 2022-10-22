import json
import boto3

def lambda_handler(event, context):
    # print("context: ",context)
    # print("event: ",event)
    client = boto3.client('lex-runtime')
    print("event: ",event)
    # data = ""
    # userId = event["aws_request_id"]
    response = client.post_text(
        botName='DiningConcierge',
        botAlias='DiningAlias',
        userId='MANDARKOL',
        inputText= event['messages'][0]['unstructured']['text']
    )
    print("response : ", response)
    message = response['message']
    botResponse = [{
        'type': 'unstructured',
        'unstructured': {
          'text': message
        }
    }]
      
    return {
        'statusCode': 200,
        'messages': botResponse
    }