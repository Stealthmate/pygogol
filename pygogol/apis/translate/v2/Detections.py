from pygogol.core import Request

from Defs import baseUrl

def detect():
    url = baseUrl + "v2/detect"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(q=None):
    url = baseUrl + "v2/detect"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
