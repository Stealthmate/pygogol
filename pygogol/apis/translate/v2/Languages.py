from pygogol.core import Request

from Defs import baseUrl

def list(model=None, target=None):
    url = baseUrl + "v2/languages"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
