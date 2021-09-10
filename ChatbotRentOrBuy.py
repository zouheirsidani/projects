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
import pandas as pd 

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

""" --- Function that returns rental and buying options --- """

def main_getoptions(RentBuy,budget):
    s3=boto3.client("s3")
    filename='Rent_OR_Buy.csv'
    bucket = "rentbuychat"
    obj = s3.get_object(Bucket= bucket, Key= filename) 
    df = pd.read_csv(obj['Body'])
    
    if RentBuy!='rent' and RentBuy!='buy':
        return ("Wrong input")
    
    output = ""
    for index, row in df.iterrows():
        if row['rent or buy']==RentBuy:
            if int(row['monthly rent or downpayment (CAD)'])<=int(budget):
                if len(output)==0:
                    output+= row['Address']+" in "+row['City']+" for the price of: "+str(row['monthly rent or downpayment (CAD)'])+"CAD"
                else:
                    output+= ", "+row['Address']+" in "+row['City']+" for the price of: "+str(row['monthly rent or downpayment (CAD)'])+"CAD"
    if len(output)==0 :
        return ("There are no options available at that budget")
    else:
        if RentBuy=="rent":
            return ('Your rental options are: '+output)
        else:
            return ('Your buying options are: '+output)
        
def return_options(intent_request):
    """
    Performs dialog management and fulfillment for returning the options.
    """
    RentBuy = intent_request['currentIntent']['slots']['RentOrBuy'].lower()
    budget = intent_request['currentIntent']['slots']['Budget']
    source = intent_request['invocationSource']
    output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
    
    if source == 'DialogCodeHook':
        # Perform basic validation on the supplied input slots.
        slots = intent_request['currentIntent']['slots']
    # return {
    #     "sessionAttributes": {},
    #     "dialogAction": {
    #         "type":"Close",
    #         "fulfillmentState":"Fulfilled",
    #         "message":{
    #             "contentType":"PlainText",
    #             "content":main_getoptions(RentBuy,budget)
    #         }
    #     }
    # }
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
    os.environ['TZ'] = 'America/Pacific'
    time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))
    return dispatch(event)
