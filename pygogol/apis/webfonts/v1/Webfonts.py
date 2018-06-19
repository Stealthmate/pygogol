from pygogol.core import Request

from Defs import baseUrl

def list(sort=None):
    url = baseUrl + "webfonts"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
