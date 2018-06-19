from pygogol.core import Request

from Defs import baseUrl

def batchGet():
    url = baseUrl + "v4/reports:batchGet"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
