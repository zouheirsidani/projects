import json
import csv
import boto3
import json
import dateutil.parser
import datetime
import time
import os
import math
import random
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }
    return response

""" --- Function that return employee name --- """

def main_getoptions(RentBuy,budget):
    s3=boto3.client("s3")
    filename='Rent_OR_Buy.csv'
    fileObj = s3.get_object(Bucket = "rentbuychat", Key=filename)
    rows = fileObj['Body'].read().decode('utf-8').split('\r\n')
        
    reader = csv.reader(rows)
    rows = []
    header = next(reader)
    for i in reader:
        rows.append(i)
        
    x=0 #row iterator
    output={}
    if RentBuy!='rent' and RentBuy!='buy':
        return ("Wrong input")
    for i in rows:
        if rows[x][0] == RentBuy: 
            if rows[x][1]<=budget:
                output[rows[x][3]]=[rows[x][1],rows[x][2]]
        x=x+1
    if not output :
        return ("There are no options available at that budget")
    else:
        if RentBuy=="rent":
            return ('Your rental options are: {}'.format(output))
        else:
            return ('Your buying options are: {}'.format(output))
        
def return_options(intent_request):
    """
    Performs dialog management and fulfillment for returning employee's department Name.
    """
    RentBuy = intent_request['currentIntent']['slots']['RentOrBuy'].lower()
    budget = intent_request['currentIntent']['slots']['Budget']
    source = intent_request['invocationSource']
    output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
    
    if source == 'DialogCodeHook':
        # Perform basic validation on the supplied input slots.
        slots = intent_request['currentIntent']['slots']
    return close(
        output_session_attributes,
        'Fulfilled',
        {
            'contentType': 'PlainText',
            'content': main_getoptions(RentBuy, budget)
        }
    )

""" --- Intents --- """
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """
    logger.debug('dispatch intentName={}'.format(intent_request['currentIntent']['name']))
    intent_name='mainintent'
    
    # Dispatch to your bot's intent handlers
    if intent_name == 'mainintent':
        return return_options(intent_request)
    raise Exception('Intent with name ' + intent_name + ' not supported')

""" --- Main handler --- """
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request as coming from the America/New_York time zone.
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))
    return dispatch(event)
