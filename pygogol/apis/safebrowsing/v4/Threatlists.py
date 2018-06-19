from pygogol.core import Request

from Defs import baseUrl

def list():
    url = baseUrl + "v4/threatLists"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
