from pygogol.core import Request

from Defs import baseUrl

def get(path=None):
    url = baseUrl + "{+path}"
    method = "GET"
    return Request(
        method, 
        url.format(['path']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(pageToken=None):
    url = baseUrl + "accounts"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(path=None, fingerprint=None):
    url = baseUrl + "{+path}"
    method = "PUT"
    return Request(
        method, 
        url.format(['path']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
