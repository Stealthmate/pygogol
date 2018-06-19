from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v4/threatHits"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
