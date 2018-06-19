from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1/shortLinks"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
