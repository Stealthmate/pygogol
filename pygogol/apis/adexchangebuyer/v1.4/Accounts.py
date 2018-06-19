from pygogol.core import Request

from Defs import baseUrl

def get(id=None):
    url = baseUrl + "accounts/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
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

def patch(id=None, confirmUnsafeAccountChange=None):
    url = baseUrl + "accounts/{id}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(id=None, confirmUnsafeAccountChange=None):
    url = baseUrl + "accounts/{id}"
    method = "PUT"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
