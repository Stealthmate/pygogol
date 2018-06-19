from pygogol.core import Request

from Defs import baseUrl

def search(query=None):
    url = baseUrl + "divisions"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
