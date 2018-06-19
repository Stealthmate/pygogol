from pygogol.core import Request

from Defs import baseUrl

def addDeal(accountId=None, buyerCreativeId=None, dealId=None):
    url = baseUrl + "creatives/{accountId}/{buyerCreativeId}/addDeal/{dealId}"
    method = "POST"
    return Request(
        method, 
        url.format(['accountId', 'buyerCreativeId', 'dealId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(accountId=None, buyerCreativeId=None):
    url = baseUrl + "creatives/{accountId}/{buyerCreativeId}"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId', 'buyerCreativeId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert():
    url = baseUrl + "creatives"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(accountId=None, buyerCreativeId=None, dealsStatusFilter=None, maxResults=None, openAuctionStatusFilter=None, pageToken=None):
    url = baseUrl + "creatives"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listDeals(accountId=None, buyerCreativeId=None):
    url = baseUrl + "creatives/{accountId}/{buyerCreativeId}/listDeals"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId', 'buyerCreativeId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def removeDeal(accountId=None, buyerCreativeId=None, dealId=None):
    url = baseUrl + "creatives/{accountId}/{buyerCreativeId}/removeDeal/{dealId}"
    method = "POST"
    return Request(
        method, 
        url.format(['accountId', 'buyerCreativeId', 'dealId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
