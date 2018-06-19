from pygogol.core import Request

from Defs import baseUrl

def get(productId=None):
    url = baseUrl + "products/{productId}"
    method = "GET"
    return Request(
        method, 
        url.format(['productId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search(pqlQuery=None):
    url = baseUrl + "products/search"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
