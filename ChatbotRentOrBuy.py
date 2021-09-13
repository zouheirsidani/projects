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


def close(fulfillment_state, message):
    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message
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
    RentBuy = intent_request['interpretations'][0]['intent']['slots']['RentOrBuy']['value']['interpretedValue'].lower()
    budget = intent_request['interpretations'][0]['intent']['slots']['Budget']['value']['interpretedValue']
    source = intent_request['invocationSource']
    
    if source == 'DialogCodeHook':
        # Perform basic validation on the supplied input slots.
        slots = intent_request['interpretations'][0]['intent']['slots']
   
    return close(
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": main_getoptions(RentBuy, budget)
        }
    )

""" --- Main handler --- """
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    os.environ['TZ'] = 'America/Pacific'
    time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))
    return return_options(event)
