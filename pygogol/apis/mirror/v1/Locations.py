from pygogol.core import Request

from Defs import baseUrl

def get(id=None):
    url = baseUrl + "locations/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list():
    url = baseUrl + "locations"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
