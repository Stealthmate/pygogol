from pygogol.core import Request

from Defs import baseUrl

def list(cid=None, format=None, model=None, q=None, source=None, target=None):
    url = baseUrl + "v2"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def translate():
    url = baseUrl + "v2"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
