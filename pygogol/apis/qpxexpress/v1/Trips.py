from pygogol.core import Request

from Defs import baseUrl

def search():
    url = baseUrl + "search"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
