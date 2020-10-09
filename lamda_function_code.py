import json
import boto3

dynamo= boto3.resource('dynamodb')
table = dynamo.Table('hourlyattendance')

def lambda_handler(event, context):
    resp = table.get_item(Key={"people_counting":event['people_counting']})
    print(resp['Item']['count'])
    count = resp['Item']['count']
    count= count+1
    inp = {"people_counting":event['people_counting'],"count":count}
    table.put_item(Item=inp)
    # TODO implement
    
    # table.put_item(Item=event)
    return "successful"
