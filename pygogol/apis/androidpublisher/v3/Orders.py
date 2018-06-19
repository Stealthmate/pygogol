from pygogol.core import Request

from Defs import baseUrl

def refund(orderId=None, packageName=None, revoke=None):
    url = baseUrl + "{packageName}/orders/{orderId}:refund"
    method = "POST"
    return Request(
        method, 
        url.format(['orderId', 'packageName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
