from pygogol.core import Request

from Defs import baseUrl

def get(accountId=None):
    url = baseUrl + "accounts/{accountId}"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(filterAdClientId=None):
    url = baseUrl + "accounts"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
