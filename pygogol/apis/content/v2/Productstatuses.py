from pygogol.core import Request

from Defs import baseUrl

def custombatch(includeAttributes=None):
    url = baseUrl + "productstatuses/batch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(merchantId=None, productId=None, destinations=None, includeAttributes=None):
    url = baseUrl + "{merchantId}/productstatuses/{productId}"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId', 'productId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(merchantId=None, destinations=None, includeAttributes=None, includeInvalidInsertedItems=None, maxResults=None, pageToken=None):
    url = baseUrl + "{merchantId}/productstatuses"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
