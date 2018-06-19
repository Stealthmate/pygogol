from pygogol.core import Request

from Defs import baseUrl

def batchGet():
    url = baseUrl + "v1/ampUrls:batchGet"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
