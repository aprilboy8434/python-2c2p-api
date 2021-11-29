#!/usr/bin/env python

import requests
import jwt
import json

merchantId = '***'
secertKey = '***'

def generatePayloadJson( secertKey, dataDict ):
    ''' Convert payload dict to json
    '''

    assert isinstance( dataDict, dict )

    encodedJwt = jwt.encode(dataDict, secertKey, algorithm="HS256")

    payloadDict = { 'payload' :  encodedJwt.decode() }

    return json.dumps(payloadDict)

if __name__ == '__main__':

    dataDict = {
                    "merchantID": merchantId,
                    "invoiceNo": '15239536611346456456',
                    "description": 'item 1',
                    "amount": 1000.00,
                    "currencyCode": 'THB'
                }

    
    data = generatePayloadJson( secertKey, dataDict )
    url = "https://sandbox-pgw.2c2p.com/payment/4.1/PaymentToken"

    headers = {
        "Accept": "text/plain",
        "Content-Type": "application/*+json"
    }

    response = requests.request("POST", url, data = data, headers=headers)


    responseDict =  json.loads(response.text)

    print( jwt.decode(responseDict['payload'], secertKey, algorithm="HS256") )
