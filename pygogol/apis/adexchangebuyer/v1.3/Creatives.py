from pygogol.core import Request

from Defs import baseUrl

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

def list(accountId=None, buyerCreativeId=None, maxResults=None, pageToken=None, statusFilter=None):
    url = baseUrl + "creatives"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
