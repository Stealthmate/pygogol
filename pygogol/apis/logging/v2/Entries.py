from pygogol.core import Request

from Defs import baseUrl

def list():
    url = baseUrl + "v2/entries:list"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def write():
    url = baseUrl + "v2/entries:write"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
