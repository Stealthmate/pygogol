from pygogol.core import Request

from Defs import baseUrl

def get(dataTransferId=None):
    url = baseUrl + "transfers/{dataTransferId}"
    method = "GET"
    return Request(
        method, 
        url.format(['dataTransferId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert():
    url = baseUrl + "transfers"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(customerId=None, maxResults=None, newOwnerUserId=None, oldOwnerUserId=None, pageToken=None, status=None):
    url = baseUrl + "transfers"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
