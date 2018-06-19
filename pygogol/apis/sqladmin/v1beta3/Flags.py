from pygogol.core import Request

from Defs import baseUrl

def list():
    url = baseUrl + "flags"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
