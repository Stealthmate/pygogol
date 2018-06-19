from pygogol.core import Request

from Defs import baseUrl

def custombatch(dryRun=None):
    url = baseUrl + "products/batch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(merchantId=None, productId=None, dryRun=None):
    url = baseUrl + "{merchantId}/products/{productId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['merchantId', 'productId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(merchantId=None, productId=None):
    url = baseUrl + "{merchantId}/products/{productId}"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId', 'productId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/products"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(merchantId=None, includeInvalidInsertedItems=None, maxResults=None, pageToken=None):
    url = baseUrl + "{merchantId}/products"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
