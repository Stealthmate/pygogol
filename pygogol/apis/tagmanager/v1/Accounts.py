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

def list():
    url = baseUrl + "accounts"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(accountId=None, fingerprint=None):
    url = baseUrl + "accounts/{accountId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['accountId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
