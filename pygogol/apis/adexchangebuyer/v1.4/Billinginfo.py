from pygogol.core import Request

from Defs import baseUrl

def get(accountId=None):
    url = baseUrl + "billinginfo/{accountId}"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list():
    url = baseUrl + "billinginfo"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
