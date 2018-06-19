from pygogol.core import Request

from Defs import baseUrl

def get(packageName=None, productId=None, token=None):
    url = baseUrl + "{packageName}/inapp/{productId}/purchases/{token}"
    method = "GET"
    return Request(
        method, 
        url.format(['packageName', 'productId', 'token']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
