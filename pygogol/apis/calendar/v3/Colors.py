from pygogol.core import Request

from Defs import baseUrl

def get():
    url = baseUrl + "colors"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
