from pygogol.core import Request

from Defs import baseUrl

def custombatch():
    url = baseUrl + "accountstatuses/batch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(accountId=None, merchantId=None, destinations=None):
    url = baseUrl + "{merchantId}/accountstatuses/{accountId}"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(merchantId=None, destinations=None, maxResults=None, pageToken=None):
    url = baseUrl + "{merchantId}/accountstatuses"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
